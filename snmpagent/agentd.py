import logging
import os
import platform
import subprocess
import sys
import tempfile

import psutil

from snmpagent import access, agent
from snmpagent import exceptions as snmp_ex

SERVICE_NAME = 'snmpagent'

LOG = logging.getLogger(__name__)


class BaseDaemon(object):
    @classmethod
    def exists(cls):
        pid_file = cls.get_pid_file()
        if os.path.exists(pid_file) and os.path.isfile(pid_file):
            with open(pid_file, 'r') as f:
                pid = int(f.read().splitlines()[0])

            try:
                process = psutil.Process(pid=pid)
                params = process.cmdline()
                if SERVICE_NAME in params[1]:
                    LOG.info(
                        "The {} process(pid={}) is already "
                        "running.".format(SERVICE_NAME, pid))
                    return True
            except psutil.NoSuchProcess:
                LOG.debug(
                    "The {} process(pid={}) is not"
                    " running.".format(SERVICE_NAME, pid))
        return False

    @classmethod
    def get_pid_file(cls):
        raise NotImplementedError(
            "Daemon needs a get_pid_file implementation.")

    @classmethod
    def stop(cls):
        pid_file = cls.get_pid_file()
        if os.path.exists(pid_file) and os.path.isfile(pid_file):
            with open(pid_file, 'r') as f:
                pid = int(f.read().splitlines()[0])

            try:
                process = psutil.Process(pid=pid)
                process.terminate()
                LOG.info("Service {}(pid={}) stopped "
                         "successfully.".format(SERVICE_NAME, pid))

            except Exception as ex:
                LOG.error(
                    "Unable to kill {}(pid={}) : {}".format(
                        SERVICE_NAME, pid, ex))
        else:
            LOG.debug("PID file %s does not exist, not started yet?")


class LinuxDaemon(BaseDaemon):
    prog_file_name = __file__

    @classmethod
    def get_pid_file(cls):
        run_path = os.path.join(os.path.dirname(__file__), 'run')
        if not os.path.exists(run_path):
            os.mkdir(run_path)
        return os.path.join(run_path, 'agent.pid')

    @classmethod
    def start(cls, conf_file):
        if cls.exists():
            return 1
        p = subprocess.Popen(
            [sys.executable, cls.prog_file_name, conf_file],
            close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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


class WindowsDaemon(BaseDaemon):
    prog_file_name = __file__

    @classmethod
    def get_pid_file(cls):
        return tempfile.gettempdir() + '\\snmp-agent.pid'

    @classmethod
    def start(cls, conf_file):
        if cls.exists():
            return 1
        DETACHED_PROCESS = 0x00000008

        p = subprocess.Popen(
            [sys.executable, WindowsDaemon.prog_file_name, conf_file],
            creationflags=DETACHED_PROCESS)
        pid = p.pid

        LOG.info(
            "Pid file path for {}: {}.".format(
                SERVICE_NAME, WindowsDaemon.get_pid_file()))
        LOG.info("Service {}(pid={}) started.".format(SERVICE_NAME, pid))

        # Create process id file to signal that
        # process has started successfully.
        with open(WindowsDaemon.get_pid_file(), 'w') as f:
            f.write(str(pid))

        LOG.debug("{} is running with pid file: {}".format(
            SERVICE_NAME, WindowsDaemon.get_pid_file()))
        return 0


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
    snmp_agent = agent.SNMPAgent(agent_conf, access.CONF_FILE_PATH)

    snmp_agent.run()


if __name__ == '__main__':
    main(sys.argv[1])
