from snmpagent_unity import access
from snmpagent_unity.commands import base
from snmpagent_unity import utils


class CreateCommunity(base.BaseCommand):
    """
Dell-EMC SNMP agent: creates a v2 community public access.

usage:
    snmpagent-unity create-community --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent-unity create-community --name user_1
    """
    name = 'create-community'

    @utils.log_command_exception
    def do(self):
        # Only support public community
        access.Access().add_v2_user(self.args['--name'])


class DeleteCommunity(base.BaseCommand):
    """
Dell-EMC SNMP agent: deletes a v2 community access.

usage:
    snmpagent-unity delete-community --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent-unity delete-community --name user_1
    """
    name = 'delete-community'

    @utils.log_command_exception
    def do(self):
        access.Access().delete_v2_user(self.args['--name'])
