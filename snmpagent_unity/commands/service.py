import logging

from snmpagent_unity import agentd, utils
from snmpagent_unity.commands import base


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
    snmpagent-unity start --conf_file <conf_file>

options:
    --conf_file <conf_file>     the agent configuration file path

examples:
    snmpagent-unity start --conf_file /tmp/agent.conf
    """
    name = 'start'
    log_to_stdout = True

    @utils.log_command_exception
    def do(self):
        _start(self.args['--conf_file'])


class Stop(base.BaseCommand):
    """
Dell-EMC SNMP agent: stops the SNMP agent.

usage:
    snmpagent-unity stop

examples:
    snmpagent-unity stop
    """
    name = 'stop'
    log_to_stdout = True

    @utils.log_command_exception
    def do(self):
        _stop()


class Restart(base.BaseCommand):
    """
Dell-EMC SNMP agent: restarts the SNMP agent.

usage:
    snmpagent-unity restart --conf_file <conf_file>

options:
    --conf_file <conf_file>     the agent configuration file path

examples:
    snmpagent-unity restart --conf_file /tmp/agent.conf
    """
    name = 'restart'
    log_to_stdout = True

    @utils.log_command_exception
    def do(self):
        _stop()
        _start(self.args['--conf_file'])
