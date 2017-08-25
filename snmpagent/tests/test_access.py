import collections
import unittest

import ddt
import mock
import os
import tempfile

import snmpagent
from snmpagent import access, config, enums
from snmpagent import exceptions as snmp_ex
from snmpagent.tests import patches


@ddt.ddt
class TestAccess(unittest.TestCase):
    @patches.user_config
    @patches.patch_get_access_path()
    def setUp(self, _):
        self.access = access.Access()

    @ddt.data({'security_level': 'invalid'},
              {'security_level': enums.SecurityLevel.AUTH_NO_PRIV,
               'auth_protocol': 'invalid'},
              {'security_level': enums.SecurityLevel.AUTH_PRIV,
               'auth_protocol': enums.AuthProtocol.MD5,
               'priv_protocol': 'invalid'})
    def test_validate_params_invalid(self, param_dict):
        self.assertRaises(snmp_ex.UserConfigError, access._validate_params,
                          **param_dict)

    @ddt.data({'security_level': enums.SecurityLevel.NO_AUTH_NO_PRIV},
              {'security_level': enums.SecurityLevel.NO_AUTH_NO_PRIV,
               'auth_protocol': enums.AuthProtocol.MD5,
               'priv_protocol': enums.PrivProtocol.AES})
    def test_validate_params_no_auth_priv(self, param_dict):
        level, auth_p, auth_k, priv_p, priv_k = access._validate_params(
            **param_dict)
        self.assertEqual(level, enums.SecurityLevel.NO_AUTH_NO_PRIV)
        self.assertIsNone(auth_p)
        self.assertIsNone(auth_k)
        self.assertIsNone(priv_p)
        self.assertIsNone(priv_k)

    @ddt.data({'security_level': enums.SecurityLevel.AUTH_PRIV,
               'auth_protocol': enums.AuthProtocol.MD5,
               'auth_key': 'key123',
               'priv_protocol': enums.PrivProtocol.AES,
               'priv_key': 'key456'})
    def test_validate_params_auth_priv(self, param_dict):
        level, auth_p, auth_k, priv_p, priv_k = access._validate_params(
            **param_dict)
        self.assertEqual(level, enums.SecurityLevel.AUTH_PRIV)
        self.assertEqual(auth_p, enums.AuthProtocol.MD5)
        self.assertEqual(auth_k, 'key123')
        self.assertEqual(priv_p, enums.PrivProtocol.AES)
        self.assertEqual(priv_k, 'key456')

    @ddt.data({'security_level': enums.SecurityLevel.AUTH_NO_PRIV,
               'auth_protocol': enums.AuthProtocol.MD5,
               'auth_key': 'key123',
               'priv_protocol': enums.PrivProtocol.AES,
               'priv_key': 'key456'})
    def test_validate_params_auth_no_priv(self, param_dict):
        level, auth_p, auth_k, priv_p, priv_k = access._validate_params(
            **param_dict)
        self.assertEqual(level, enums.SecurityLevel.AUTH_NO_PRIV)
        self.assertEqual(auth_p, enums.AuthProtocol.MD5)
        self.assertEqual(auth_k, 'key123')
        self.assertIsNone(priv_p)
        self.assertIsNone(priv_k)

    def test_add_v3_user_exist(self):
        name = 'existing'
        self.access.user_conf.entries = {name: name}
        self.assertRaises(snmp_ex.UserExistingError, self.access.add_v3_user,
                          name, enums.SecurityLevel.AUTH_PRIV)

    @patches.user_v3_entry
    def test_add_v3_user(self, user_v3_entry):
        self.access.user_conf.entries = {}
        self.access.add_v3_user('user_1', enums.SecurityLevel.AUTH_PRIV,
                                auth_protocol=enums.AuthProtocol.MD5,
                                auth_key='key123',
                                priv_protocol=enums.PrivProtocol.AES,
                                priv_key='key456')

        user_v3_entry.assert_called_with('user_1', None,
                                         enums.SecurityLevel.AUTH_PRIV,
                                         enums.AuthProtocol.MD5, 'key123',
                                         enums.PrivProtocol.AES, 'key456')
        self.assertIn('user_1', self.access.user_conf.entries)

    def test_add_v2_user_exist(self):
        name = 'existing'
        self.access.user_conf.entries = {name: name}
        self.assertRaises(snmp_ex.UserExistingError, self.access.add_v2_user,
                          name)

    @patches.user_v2_entry
    def test_add_v2_user(self, user_v2_entry):
        self.access.user_conf.entries = {}
        self.access.add_v2_user('user_1')

        user_v2_entry.assert_called_with('user_1', 'user_1')
        self.assertIn('user_1', self.access.user_conf.entries)

    def test_add_v2_user_already_exists(self):
        self.access.user_conf.entries = {'user-public': {}}
        self.assertRaises(snmp_ex.UserExistingError,
                          self.access.add_v2_user, 'user-public')

    def test_delete_v3_user(self):
        name = 'user_1'
        self.access.user_conf.entries = {name: name}
        self.access.delete_v3_user(name)
        self.assertNotIn(name, self.access.user_conf.entries)

    def test_delete_v3_user_not_exist(self):
        name = 'not-existing'
        self.access.user_conf.entries = {}
        self.assertRaises(snmp_ex.UserNotExistsError,
                          self.access.delete_v3_user,
                          name)
        self.access.user_conf.save.assert_not_called()

    def test_delete_v2_user(self):
        name = 'user_1'
        self.access.user_conf.entries = {name: name}
        self.access.delete_v2_user(name)
        self.assertNotIn(name, self.access.user_conf.entries)

    def test_delete_v2_user_not_exist(self):
        name = 'not-existing'
        self.access.user_conf.entries = {}
        self.assertRaises(snmp_ex.UserNotExistsError,
                          self.access.delete_v2_user,
                          name)
        self.access.user_conf.save.assert_not_called()

    def test_update_v3_user_not_exist(self):
        name = 'not-existing'
        self.access.user_conf.entries = {}
        self.assertRaises(snmp_ex.UserNotExistsError,
                          self.access.update_v3_user,
                          name)

    def test_update_v3_user(self):
        name = 'user_1'
        old_user = config.UserV3ConfigEntry(name, None,
                                            enums.SecurityLevel.AUTH_PRIV,
                                            enums.AuthProtocol.SHA, 'key123',
                                            enums.PrivProtocol.AES, 'key456')
        self.access.user_conf.entries = {name: old_user}
        self.access.update_v3_user(name, auth_protocol=enums.AuthProtocol.MD5,
                                   priv_key='key789')
        new_user = self.access.user_conf.entries[name]
        self.assertEqual(name, new_user.name)
        self.assertEqual(enums.SecurityLevel.AUTH_PRIV,
                         new_user.security_level)
        self.assertEqual(enums.AuthProtocol.MD5, new_user.auth_protocol)
        self.assertEqual('key123', new_user.auth_key.raw)
        self.assertEqual(enums.PrivProtocol.AES, new_user.priv_protocol)
        self.assertEqual('key789', new_user.priv_key.raw)
        self.access.user_conf.save.assert_called_once()

    def test_list_users(self):
        users = collections.OrderedDict()
        users['user_1'] = config.UserV2ConfigEntry(
            'user_1', enums.Community.PUBLIC)
        users['user_2'] = config.UserV2ConfigEntry(
            'user_2', enums.Community.PUBLIC)
        users['user_3'] = config.UserV3ConfigEntry(
            'user_3', '-', enums.SecurityLevel.AUTH_PRIV,
            enums.AuthProtocol.MD5, 'key123', enums.PrivProtocol.AES,
            'key456')
        users['user_4'] = config.UserV3ConfigEntry(
            'user_4', '-', enums.SecurityLevel.AUTH_NO_PRIV,
            enums.AuthProtocol.SHA, 'key123', None, None)
        self.access.user_conf.entries = users

        expected = '''SNMP Version 2 Community Access:
user_1
    Version:    SNMPv2c
    Community:  user_1
user_2
    Version:    SNMPv2c
    Community:  user_2

SNMP Version 3 Users:
user_3
    Version:            SNMPv3
    Security Level:     authPriv
    Auth Protocol:      MD5
    Auth Key:           34a0323fa11e5432ebe681b103de1fa5\x06
    Privacy Protocol:   AES
    Privacy Key:        040591c13f4a9d3b470f108493d26b0f\x06
user_4
    Version:            SNMPv3
    Security Level:     authNoPriv
    Auth Protocol:      SHA
    Auth Key:           34a0323fa11e5432ebe681b103de1fa5\x06
    Privacy Protocol:   -
    Privacy Key:        -
'''
        with patches.stdout() as out:
            self.access.list_users()
        output = out.getvalue()
        self.assertEqual(output, expected)

    def test_get_access_path(self):
        with mock.patch('os.path.expanduser') as my_path:
            my_path.return_value = os.path.join(
                os.path.join(os.path.dirname(__file__),
                             'test_data', 'configs'))
            access_path = access.get_access_data_path()
            self.assertTrue('access.db' in access_path)

    def test_get_access_path_create_dir(self):
        temp_path = os.path.join(tempfile.gettempdir(),
                                 '.{}'.format(snmpagent.SERVICE_NAME))
        if os.path.exists(os.path.join(temp_path, 'access.db')):
            os.remove(os.path.join(temp_path, 'access.db'))
        if os.path.isdir(temp_path):
            os.removedirs(temp_path)

        with mock.patch('os.path.expanduser') as my_path:
            my_path.return_value = temp_path
            access_path = access.get_access_data_path()
            self.assertTrue(temp_path in access_path)
