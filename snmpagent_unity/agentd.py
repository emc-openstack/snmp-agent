import logging
import os
import platform
import subprocess
import sys
import tempfile

import psutil

from snmpagent_unity import access, agent
from snmpagent_unity import config as snmp_config
from snmpagent_unity import exceptions as snmp_ex

SERVICE_NAME = 'snmpagent-unity'

LOG = logging.getLogger(__name__)


class BaseDaemon(object):
    @classmethod
    def validate_conf(cls, agent_conf_file):
        access_conf_file = access.get_access_data_path()
        snmp_config.AgentConfig(agent_conf_file).raise_if_error()
        snmp_config.UserConfig(access_conf_file).raise_if_error()

    @classmethod
    def exists(cls):
        pid_file = cls.get_pid_file()
        if os.path.exists(pid_file) and os.path.isfile(pid_file):
            with open(pid_file, 'r') as f:
                pid = int(f.read().splitlines()[0])

            try:
                process = psutil.Process(pid=pid)
                params = process.cmdline()
                if 'agentd.py' in params[1]:
                    LOG.debug(
                        "The {} process(pid={}) is already "
                        "running.".format(SERVICE_NAME, pid))
                    return process
            except psutil.NoSuchProcess:
                LOG.debug(
                    "The {} process(pid={}) is not"
                    " running.".format(SERVICE_NAME, pid))
            else:
                LOG.debug(
                    "The process(pid={}) doesn't look like a {} service. "
                    "Not stopping it.".format(pid, SERVICE_NAME))
        return None

    @classmethod
    def get_pid_file(cls):
        return os.path.join(tempfile.gettempdir(), 'snmpagent-unity.pid')

    @classmethod
    def _launch_process(cls, conf_file):
        raise NotImplementedError()

    @classmethod
    def start(cls, conf_file):
        if cls.exists():
            return 1
        cls.validate_conf(conf_file)
        p = cls._launch_process(conf_file)
        pid = p.pid

        LOG.info(
            "{} pid file path: {}.".format(SERVICE_NAME, cls.get_pid_file()))
        LOG.info("Service {}(pid={}) started.".format(SERVICE_NAME, pid))

        # Create process id file to signal that
        # process has started successfully.
        with open(cls.get_pid_file(), 'w') as f:
            f.write(str(pid))

        LOG.debug("{} is running with pid file: {}".format(
            SERVICE_NAME, cls.get_pid_file()))
        return 0

    @classmethod
    def stop(cls):
        process = cls.exists()
        if process:
            try:
                process.terminate()
                LOG.info("Service {}(pid={}) stopped "
                         "successfully.".format(SERVICE_NAME, process.pid))
                ret = 0
                os.remove(cls.get_pid_file())
            except Exception as ex:
                LOG.error(
                    "Unable to kill {}(pid={}) : {}".format(
                        SERVICE_NAME, process.pid, ex))
                ret = 1
        else:
            LOG.info("Agent service does not exist, not started yet?")
            ret = 1
        return ret


class LinuxDaemon(BaseDaemon):
    prog_file_name = __file__

    @classmethod
    def _launch_process(cls, conf_file):
        return subprocess.Popen(
            [sys.executable, cls.prog_file_name, conf_file],
            close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class WindowsDaemon(BaseDaemon):
    prog_file_name = __file__

    @classmethod
    def _launch_process(cls, conf_file):
        DETACHED_PROCESS = 0x00000008
        return subprocess.Popen(
            [sys.executable, WindowsDaemon.prog_file_name, conf_file],
            creationflags=DETACHED_PROCESS)


NAME = 'Dell EMC SNMP Agent Daemon'

if platform.system() == 'Windows':
    agent_daemon = WindowsDaemon
elif platform.system() == 'Linux':
    agent_daemon = LinuxDaemon
else:
    raise snmp_ex.NotSupportedPlatformError(
        'Not supported platform: {}'.format(platform.system()))


def main(agent_conf=None):
    """Main entry for running agent on Windows.

    When running within a detached process, it acts as
    a daemon for SNMP background processing.
    """
    if not agent_conf:
        agent_conf = os.path.abspath('configs/agent.conf')
    snmp_agent = agent.SNMPAgent(agent_conf, access.get_access_data_path())

    snmp_agent.run()


if __name__ == '__main__':
    main(sys.argv[1])
