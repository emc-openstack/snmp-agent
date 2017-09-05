import docopt

from snmpagent_unity import access, enums
from snmpagent_unity import exceptions as snmp_ex
from snmpagent_unity import utils
from snmpagent_unity.commands import base


def get_args(args):
    return (args['--name'], args['--auth'], args['--auth_key'], args['--priv'],
            args['--priv_key'])


def check_length(string):
    if 8 <= len(string) <= 24:
        return True
    return False


class AddUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: Add a v3 user.

usage:
    snmpagent-unity add-user --name <name> --auth <auth_protocol> --auth_key \
<auth_key> [--priv <priv_protocol>] [--priv_key <priv_key>]

options:
    --name <name>               the user name
    --auth <auth_protocol>      the authentication protocol (MD5 or SHA)
    --auth_key <auth_key>       the authentication password \
(length: 8 to 24 characters)
    --priv <priv_protocol>      the privacy protocol (AES or DES)
    --priv_key <priv_key>       the privacy password \
(length: 8 to 24 characters)

examples:
    snmpagent-unity add-user --name user_1 --auth md5 --auth_key authkey123 \
--priv des --priv_key privkey123
    """
    name = 'add-user'

    @utils.log_command_exception
    def do(self):
        name, auth, auth_key, priv, priv_key = get_args(self.args)

        if bool(priv) != bool(priv_key):
            raise docopt.DocoptExit('One of `priv` and `priv_key` is missing.')
        if priv and priv_key:
            level = enums.SecurityLevel.AUTH_PRIV
        else:
            level = enums.SecurityLevel.AUTH_NO_PRIV

        if not check_length(auth_key):
            raise snmp_ex.UserInvalidPasswordError(
                'Auth key length is {}, should be 8 to 24 '
                'characters'.format(len(auth_key)))
        if priv_key and not check_length(priv_key):
            raise snmp_ex.UserInvalidPasswordError(
                'Priv key length is {}, should be 8 to 24 '
                'characters'.format(len(priv_key)))

        access.Access().add_v3_user(
            name, level, auth, auth_key, priv, priv_key)


class UpdateUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: Update the info of a v3 user.

usage:
    snmpagent-unity update-user --name <name> [--auth <auth_protocol>] \
[--auth_key <auth_key>] [--priv <priv_protocol>] [--priv_key <priv_key>]

options:
    --name <name>               the user name
    --auth <auth_protocol>      the authentication protocol (MD5 or SHA)
    --auth_key <auth_key>       the authentication password \
(length: 8 to 24 characters)
    --priv <priv_protocol>      the privacy protocol (AES or DES)
    --priv_key <priv_key>       the privacy password \
(length: 8 to 24 characters)

examples:
    snmpagent-unity update-user --name user_1 --auth md5 --auth_key \
authkey123 --priv des --priv_key privkey123
    """
    name = 'update-user'

    @utils.log_command_exception
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

        if not check_length(auth_key):
            raise snmp_ex.UserInvalidPasswordError(
                'Auth key length is {}, should be 8 to 24 '
                'characters'.format(len(auth_key)))
        if priv_key and not check_length(priv_key):
            raise snmp_ex.UserInvalidPasswordError(
                'Priv key length is {}, should be 8 to 24 '
                'characters'.format(len(priv_key)))

        access.Access().update_v3_user(name, level, auth, auth_key, priv,
                                       priv_key)


class DeleteUser(base.BaseCommand):
    """
Dell-EMC SNMP agent: Delete a v3 user.

usage:
    snmpagent-unity delete-user --name <name>

options:
    --name <name>               the user name

examples:
    snmpagent-unity delete-user --name user_1
    """
    name = 'delete-user'

    @utils.log_command_exception
    def do(self):
        access.Access().delete_v3_user(self.args['--name'])


class ListUsers(base.BaseCommand):
    """
Dell-EMC SNMP agent: List all the users, including the v2 community access.

usage:
    snmpagent-unity list-users

examples:
    snmpagent-unity list-users
    """
    name = 'list-users'

    @utils.log_command_exception
    def do(self):
        access.Access().list_users()
