from snmpagent import config
from snmpagent.commands import base


class Encrypt(base.BaseCommand):
    """
Dell-EMC SNMP agent: encrypts the configuration file.

usage:
    snmpagent encrypt --conf_file <conf_file>

options:
    --conf_file <conf_file>     the configuration file to be encrypted

examples:
    snmpagent encrypt --conf_file /tmp/agent.conf
    """
    name = 'encrypt'

    def do(self):
        agent_config = config.AgentConfig(self.args['--conf_file'])
        agent_config.save()


class Decrypt(base.BaseCommand):
    """
Dell-EMC SNMP agent: decrypts the configuration file.

usage:
    snmpagent decrypt --conf_file <conf_file>

options:
    --conf_file <conf_file>     the configuration file to be decrypted

examples:
    snmpagent decrypt --conf_file /tmp/agent.conf
    """
    name = 'decrypt'

    def do(self):
        agent_config = config.AgentConfig(self.args['--conf_file'])
        agent_config.save(encrypt=False)
