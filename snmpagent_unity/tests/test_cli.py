import re
import unittest

import ddt
import mock
from snmpagent_unity import cli, enums
from snmpagent_unity.commands import base
from snmpagent_unity.tests import patches


@ddt.ddt
class TestCli(unittest.TestCase):
    @mock.patch('docopt.docopt')
    def test_cli_base(self, _):
        base_cmd = base.BaseCommand([],
                                    {'--log_file': None, '--log_level': None})
        self.assertRaises(NotImplementedError, base_cmd.do)

    @patches.sys_argv(['snmpagent-unity', '--help'],
                      ['snmpagent-unity', 'add-user', '--help'])
    def test_cli_help(self, _):
        with self.assertRaises(SystemExit) as raised:
            cli.main()
        err = raised.exception
        self.assertFalse(err.code)

    @patches.sys_argv(['snmpagent-unity'],
                      ['snmpagent-unity', 'add-user'],
                      ['snmpagent-unity', 'add-user', '--name'],
                      ['snmpagent-unity', 'add-user', '--name', 'user_1'],
                      ['snmpagent-unity', 'add-user', '--name', 'user_1',
                       '--auth'],
                      ['snmpagent-unity', 'add-user', '--name', 'user_1',
                       '--auth_key'])
    def test_cli_usage(self, _):
        with self.assertRaises(SystemExit) as raised:
            cli.main()
        err = raised.exception
        self.assertTrue('usage:' in err.code.split('\n'))

    @patches.sys_argv(['snmpagent-unity', 'abc'])
    def test_cli_not_supported(self, _):
        with self.assertRaises(SystemExit) as raised:
            cli.main()
        err = raised.exception
        self.assertTrue(err.code.startswith('Not supported command: '))

    @patches.sys_argv(
        ['snmpagent-unity', 'add-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv', 'des'],
        ['snmpagent-unity', 'add-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv_key', 'privkey456'])
    def test_cli_add_user_priv_invalid(self, _):
        with self.assertRaises(SystemExit) as raised:
            cli.main()
        err = raised.exception
        self.assertTrue(
            err.code.startswith('One of `priv` and `priv_key` is missing.'))

    @patches.sys_argv(
        ['snmpagent-unity', 'add-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv', 'des', '--priv_key',
         'privkey456'])
    @patches.access
    def test_cli_add_user_auth_priv(self, _, mocked_access):
        cli.main()
        mocked_access().add_v3_user.assert_called_with(
            'user_1', enums.SecurityLevel.AUTH_PRIV, 'md5', 'authkey123',
            'des', 'privkey456')

    @patches.sys_argv(
        ['snmpagent-unity', 'add-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123'])
    @patches.access
    def test_cli_add_user_auth_no_priv(self, _, mocked_access):
        cli.main()
        mocked_access().add_v3_user.assert_called_with(
            'user_1', enums.SecurityLevel.AUTH_NO_PRIV, 'md5',
            'authkey123', None, None)

    @patches.sys_argv(
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth', 'md5',
         '--priv', 'des', '--priv_key', 'privkey456'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth_key',
         'authkey123', '--priv', 'des', '--priv_key', 'privkey456'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth',
         'md5'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth_key',
         'authkey123'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv', 'des'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv_key', 'privkey456'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--priv',
         'des'],
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--priv_key',
         'privkey456'])
    def test_cli_update_user_args_invalid(self, _):
        with self.assertRaises(SystemExit) as raised:
            cli.main()
        err = raised.exception
        self.assertTrue(
            re.match('One of `(priv|auth)` and `(priv|auth)_key` is missing.',
                     err.code))

    @patches.sys_argv(
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123', '--priv', 'des', '--priv_key',
         'privkey456'])
    @patches.access
    def test_cli_update_user_auth_priv(self, _, mocked_access):
        cli.main()
        mocked_access().update_v3_user.assert_called_with(
            'user_1', enums.SecurityLevel.AUTH_PRIV, 'md5', 'authkey123',
            'des',
            'privkey456')

    @patches.sys_argv(
        ['snmpagent-unity', 'update-user', '--name', 'user_1', '--auth', 'md5',
         '--auth_key', 'authkey123'])
    @patches.access
    def test_cli_update_user_auth_no_priv(self, _, mocked_access):
        cli.main()
        mocked_access().update_v3_user.assert_called_with(
            'user_1', enums.SecurityLevel.AUTH_NO_PRIV, 'md5', 'authkey123',
            None,
            None)

    @patches.sys_argv(['snmpagent-unity', 'delete-user', '--name', 'user_1'])
    @patches.access
    def test_cli_delete_user(self, _, mocked_access):
        cli.main()
        mocked_access().delete_v3_user.assert_called_with('user_1')

    @patches.sys_argv(['snmpagent-unity', 'list-users'])
    @patches.access
    def test_cli_list_users(self, _, mocked_access):
        cli.main()
        mocked_access().list_users.assert_called_with()

    @patches.sys_argv(
        ['snmpagent-unity', 'create-community', '--name', 'user_1'])
    @patches.access
    def test_cli_create_community(self, _, mocked_access):
        cli.main()
        mocked_access().add_v2_user.assert_called_with('user_1')

    @patches.sys_argv(
        ['snmpagent-unity', 'delete-community', '--name', 'user_1'])
    @patches.access
    def test_cli_delete_community(self, _, mocked_access):
        cli.main()
        mocked_access().delete_v2_user.assert_called_with('user_1')

    @patches.sys_argv(
        ['snmpagent-unity', 'encrypt', '--conf_file', '/tmp/agent.conf'])
    @patches.agent_config
    def test_cli_encrypt(self, _, mocked_config):
        cli.main()
        mocked_config.save.assert_called_with()

    @patches.sys_argv(
        ['snmpagent-unity', 'decrypt', '--conf_file', '/tmp/agent.conf'])
    @patches.agent_config
    def test_cli_decrypt(self, _, mocked_config):
        cli.main()
        mocked_config.save.assert_called_with(encrypt=False)
