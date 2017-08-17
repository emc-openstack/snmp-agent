import logging
import multiprocessing
import platform

from snmpagent import agentd
from snmpagent.commands import base


def get_log_handlers():
    return [handler.stream for handler in logging.getLogger('').handlers if
            isinstance(handler, logging.FileHandler)]


def _start(conf_file):
    agentd.agent_daemon.start(conf_file)


def _stop():
    agentd.agent_daemon.stop()


class Start(base.BaseCommand):
    """
Dell-EMC SNMP agent: starts the SNMP agent.

usage:
    snmpagent start --conf_file <conf_file>

options:
    --conf_file <conf_file>     the agent configuration file path

examples:
    snmpagent start --conf_file /tmp/agent.conf
    """
    name = 'start'
    log_to_stdout = True

    def do(self):
        _start(self.args['--conf_file'])


class Stop(base.BaseCommand):
    """
Dell-EMC SNMP agent: stops the SNMP agent.

usage:
    snmpagent stop

examples:
    snmpagent stop
    """
    name = 'stop'
    log_to_stdout = True

    def do(self):
        _stop()


class Restart(base.BaseCommand):
    """
Dell-EMC SNMP agent: restarts the SNMP agent.

usage:
    snmpagent restart --conf_file <conf_file>

options:
    --conf_file <conf_file>     the agent configuration file path

examples:
    snmpagent restart --conf_file /tmp/agent.conf
    """
    name = 'restart'
    log_to_stdout = True

    def do(self):
        _stop()
        _start(self.args['--conf_file'])
