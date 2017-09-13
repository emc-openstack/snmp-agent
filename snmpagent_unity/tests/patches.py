import os
import shutil
import sys
import tempfile
from contextlib import contextmanager

from snmpagent_unity import clients

from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity import engine

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import ddt
import mock
from snmpagent_unity.tests import mocks

DEFAULT = mock.DEFAULT


def sys_argv(*ddt_data):
    def _dec(func):
        @ddt.data(*ddt_data)
        def _inner(test_clz, *args):
            temp = sys.argv
            sys.argv = args[0]
            func(test_clz, args)
            sys.argv = temp

        return _inner

    return _dec


access = mock.patch('snmpagent_unity.access.Access')

FAKE_ACCESS_FILE = os.path.join(os.path.dirname(__file__),
                                'test_data', 'configs', 'access.db')


def patch_get_access_path(new_path=FAKE_ACCESS_FILE):
    def _inner(test_case):
        def func(*args, **kwargs):
            with mock.patch(
                    'snmpagent_unity.access.get_access_data_path',
                    new=mock.Mock(return_value=new_path)):
                test_case(*args, **kwargs)

        return func

    return _inner


def patch_config(config_type):
    def _dec(func):
        def _inner(test_clz, *args):
            with mock.patch('snmpagent_unity.config.{}'.format(config_type)) \
                    as tmp_patch:
                mocked = mock.Mock()
                tmp_patch.return_value = mocked
                args = args + (mocked,)
                func(test_clz, *args)

        return _inner

    return _dec


def patch_get_pid_file(func):
    def _inner(*args, **kwargs):
        with mock.patch('snmpagent_unity.agentd.BaseDaemon.get_pid_file') \
                as fake:
            fake.return_value = os.path.join(tempfile.gettempdir(),
                                             "fake_snmpagent.pid")
            return func(*args, **kwargs)

    return _inner


class FakePopen(object):
    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

    def __init__(self):
        self.pid = 1111


agent_config = patch_config('AgentConfig')
user_config = patch_config('UserConfig')
agent_config_entry = mock.patch('snmpagent_unity.config.AgentConfigEntry')
user_v3_entry = mock.patch('snmpagent_unity.config.UserV3ConfigEntry')
user_v2_entry = mock.patch('snmpagent_unity.config.UserV2ConfigEntry')

unity_client = mock.patch('snmpagent_unity.clients.UnityClient')
unity_system = mock.patch(target='snmpagent_unity.clients.storops.UnitySystem',
                          new=mocks.MockUnitySystem)

mock_engine = mock.patch.multiple(engine.SnmpEngine,
                                  registerTransportDispatcher=DEFAULT)
mock_client = mock.patch.multiple(clients.UnityClient,
                                  get_unity_client=DEFAULT)
mock_udp = mock.patch.multiple(udp.UdpTransport, openServerMode=DEFAULT)

add_transport = mock.patch('snmpagent_unity.agent.config.addTransport')
add_v1_system = mock.patch('snmpagent_unity.agent.config.addV1System')
add_v3_user = mock.patch('snmpagent_unity.agent.config.addV3User')
add_vacm_user = mock.patch('snmpagent_unity.agent.config.addVacmUser')

subprocess = mock.patch('subprocess.Popen', new_callable=FakePopen)
psutil_process = mock.patch('psutil.Process')


@contextmanager
def stdout():
    new_stdout, old_stdout = StringIO(), sys.stdout
    try:
        sys.stdout = new_stdout
        yield sys.stdout
    finally:
        sys.stdout = old_stdout


def conf_data(*conf_paths):
    def dec(func):
        def _inner(test_ref, *args):
            temp_dir = tempfile.mkdtemp()
            for conf_path in conf_paths:
                shutil.copy(conf_path, temp_dir)
            confs = [os.path.join(temp_dir, os.path.basename(conf_path))
                     for conf_path in conf_paths]
            func(test_ref, *confs)
            shutil.rmtree(temp_dir)

        return _inner

    return dec
