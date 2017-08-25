import logging

from snmpagent import config, utils
from snmpagent.commands import base

LOG = logging.getLogger(__file__)


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

    @utils.log_command_exception
    def do(self):
        agent_config = config.AgentConfig(self.args['--conf_file'])
        agent_config.save()
        LOG.info("Encrypted config file '{}' successfully.".format(
            self.args['--conf_file']))


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

    @utils.log_command_exception
    def do(self):
        agent_config = config.AgentConfig(self.args['--conf_file'])
        agent_config.save(encrypt=False)
        LOG.info("Decrypted config file '{}' successfully.".format(
            self.args['--conf_file']))
