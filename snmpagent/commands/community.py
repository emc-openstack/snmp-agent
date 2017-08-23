from snmpagent import access
from snmpagent.commands import base
from snmpagent import utils


class CreateCommunity(base.BaseCommand):
    """
Dell-EMC SNMP agent: creates a v2 community public access.

usage:
    snmpagent create-community --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent create-community --name user_1
    """
    name = 'create-community'

    @utils.log_command_exception
    def do(self):
        # Only support public community
        access.access.add_v2_user(self.args['--name'])


class DeleteCommunity(base.BaseCommand):
    """
Dell-EMC SNMP agent: deletes a v2 community access.

usage:
    snmpagent delete-community --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent delete-community --name user_1
    """
    name = 'delete-community'

    @utils.log_command_exception
    def do(self):
        access.access.delete_v2_user(self.args['--name'])
