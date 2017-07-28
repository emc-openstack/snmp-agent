import multiprocessing
import os

import psutil
from snmpagent import agentd
from snmpagent.commands import base


def get_pid_file():
    run_path = os.path.join(os.path.dirname(__file__), '..', 'run')
    if not os.path.exists(run_path):
        os.mkdir(run_path)
    return os.path.join(run_path, 'agent.pid')


def _start(conf_file):
    p = multiprocessing.Process(target=agentd.agent_daemon.start,
                                name=agentd.NAME,
                                kwargs={'pid_file': get_pid_file(),
                                        'agent_conf': conf_file})
    p.start()


def _stop():
    pid_file = get_pid_file()
    if os.path.isfile(pid_file) and os.path.exists(pid_file):
        with open(pid_file, 'r') as f:
            pid = int(f.read().splitlines()[0])
        process = psutil.Process(pid=pid)
        process.terminate()


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
    log_to_stdout = False

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
    log_to_stdout = False

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
    log_to_stdout = False

    def do(self):
        _stop()
        _start(self.args['--conf_file'])
