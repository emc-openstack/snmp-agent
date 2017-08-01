import docopt

from snmpagent import access, enums
from snmpagent.commands import base


def get_args(args):
    return (args['--name'], args['--auth'], args['--auth_key'], args['--priv'],
            args['--priv_key'])


class AddUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: adds a v3 user.

usage:
    snmpagent add-user --name <name> --auth <auth_protocol> --auth_key \
<auth_key> [--priv <priv_protocol>] [--priv_key <priv_key>]

options:
    --name <name>               the user name
    --auth <auth_protocol>      the authentication protocol
    --auth_key <auth_key>       the authentication password
    --priv <priv_protocol>      the privacy protocol
    --priv_key <priv_key>       the privacy password

examples:
    snmpagent add-user --name user_1 --auth md5 --auth_key key123 \
--priv des --priv_key key456
    """
    name = 'add-user'

    def do(self):
        name, auth, auth_key, priv, priv_key = get_args(self.args)

        if bool(priv) != bool(priv_key):
            raise docopt.DocoptExit('One of `priv` and `priv_key` is missing.')
        if priv and priv_key:
            level = enums.SecurityLevel.AUTH_PRIV
        else:
            level = enums.SecurityLevel.AUTH_NO_PRIV
        access.access.add_v3_user(name, level, auth, auth_key, priv, priv_key)


class UpdateUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: updates the info of a v3 user.

usage:
    snmpagent update-user --name <name> [--auth <auth_protocol>] \
[--auth_key <auth_key>] [--priv <priv_protocol>] [--priv_key <priv_key>]

options:
    --name <name>               the user name
    --auth <auth_protocol>      the authentication protocol
    --auth_key <auth_key>       the authentication password
    --priv <priv_protocol>      the privacy protocol
    --priv_key <priv_key>       the privacy password

examples:
    snmpagent update-user --name user_1 --auth md5 --auth_key key123 \
--priv des --priv_key key456
    """
    name = 'update-user'

    def do(self):
        name, auth, auth_key, priv, priv_key = get_args(self.args)

        if bool(auth) != bool(auth_key):
            raise docopt.DocoptExit('One of `auth` and `auth_key` is missing.')
        if bool(priv) != bool(priv_key):
            raise docopt.DocoptExit('One of `priv` and `priv_key` is missing.')

        if priv and priv_key:
            level = enums.SecurityLevel.AUTH_PRIV
        else:
            level = enums.SecurityLevel.AUTH_NO_PRIV
        access.access.update_v3_user(name, level, auth, auth_key, priv,
                                     priv_key)


class DeleteUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: deletes a v3 user.

usage:
    snmpagent delete-user --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent delete-user --name user_1
    """
    name = 'delete-user'

    def do(self):
        access.access.delete_v3_user(self.args['--name'])


class ListUsers(base.BaseCommand):
    """
Dell-EMC SNMP agent: lists all the users, including the v2 community access.

usage:
    snmpagent list-users

examples:
    snmpagent list-users
    """
    name = 'list-users'

    def do(self):
        access.access.list_users()
