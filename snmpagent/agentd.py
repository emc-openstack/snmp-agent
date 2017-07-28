import logging
import platform

import daemon
from daemon import pidfile
from snmpagent import access, agent
from snmpagent import exceptions as snmp_ex

LOG = logging.getLogger(__name__)


class LinuxDaemon(object):
    @staticmethod
    def _action(agent_conf):
        # from pdbx import Rpdb; rpdb = Rpdb(8787); rpdb.set_trace()
        agent.SNMPAgent(agent_conf, access.CONF_FILE_PATH).run()

    @staticmethod
    def start(pid_file, agent_conf):
        with daemon.DaemonContext(
                umask=0o002, pidfile=pidfile.TimeoutPIDLockFile(pid_file)):
            LinuxDaemon._action(agent_conf)


NAME = 'Dell EMC SNMP Agent Daemon'

if platform.system() == 'Windows':
    agent_daemon = None
elif platform.system() == 'Linux':
    agent_daemon = LinuxDaemon
else:
    raise snmp_ex.NotSupportedPlatformError(
        'Not supported platform: {}'.format(platform.system()))
