import os
import shutil
import sys
import tempfile
from contextlib import contextmanager

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import ddt
import mock


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


access = mock.patch('snmpagent.access.access')


def patch_config(config_type):
    def _dec(func):
        def _inner(test_clz, *args):
            with mock.patch('snmpagent.config.' + config_type) as tmp_patch:
                mocked = mock.Mock()
                tmp_patch.return_value = mocked
                args = args + (mocked,)
                func(test_clz, *args)

        return _inner

    return _dec


agent_config = patch_config('AgentConfig')
user_config = patch_config('UserConfig')
user_v3_entry = mock.patch('snmpagent.config.UserV3ConfigEntry')
user_v2_entry = mock.patch('snmpagent.config.UserV2ConfigEntry')


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
