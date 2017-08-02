# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from snmpagent import config, cipher
from snmpagent.tests import patches, utils


class TestConfig(unittest.TestCase):
    @patches.conf_data(utils.conf_full_path('agent.conf'))
    def test_agent_config(self, conf_file):
        conf = config.AgentConfig(conf_file)
        self.assertEqual(2, len(conf.entries))
        for name, entry in conf.entries.items():
            self.assertEqual('0.0.0.0', entry.agent_ip)
            if name == 'unity-1':
                self.assertEqual('11161', entry.agent_port)
                self.assertEqual('unity', entry.model)
                self.assertEqual('10.10.10.21', entry.mgmt_ip)
                self.assertEqual('admin', entry.user)
                self.assertEqual('Password21', entry.password.raw)
            elif name == 'unity-2':
                self.assertEqual('11162', entry.agent_port)
                self.assertEqual('unity', entry.model)
                self.assertEqual('10.10.10.22', entry.mgmt_ip)
                self.assertEqual('admin', entry.user)
                self.assertEqual('Password22!', entry.password.raw)
            else:
                self.assertFalse(True)

    @patches.conf_data(utils.conf_full_path('agent.conf'))
    def test_agent_config_save_reload(self, conf_file):

        def _read_passwd(conf_file):
            pattern = ('password=', 'password = ')
            with open(conf_file, 'r') as f:
                return [line.split('=')[1].strip() for line in f.readlines()
                        if line.startswith(pattern)]

        conf = config.AgentConfig(conf_file)
        conf.save()
        encrypt_passwds = _read_passwd(conf_file)
        self.assertEqual(len(encrypt_passwds), 2)
        for passwd in encrypt_passwds:
            self.assertTrue(cipher.is_encrypted(passwd))

        self.test_agent_config(conf_file)

    @patches.conf_data(utils.conf_full_path('access.conf'))
    def test_user_config(self, conf_file):
        conf = config.UserConfig(conf_file)
        self.assertEqual(3, len(conf.entries))
        for name, entry in conf.entries.items():
            if name == 'user-md5-des':
                self.assertEqual('user-md5-des', entry.name)
                self.assertEqual('SNMPv3', entry.mode.value)
                self.assertEqual('', entry.context)
                self.assertEqual('authPriv', entry.security_level.value)
                self.assertEqual('MD5', entry.auth_protocol.value)
                self.assertEqual('authkey1', entry.auth_key.raw)
                self.assertEqual('DES', entry.priv_protocol.value)
                self.assertEqual('privkey1', entry.priv_key.raw)
            elif name == 'user-sha-none':
                self.assertEqual('user-sha-none', entry.name)
                self.assertEqual('SNMPv3', entry.mode.value)
                self.assertEqual('', entry.context)
                self.assertEqual('authNoPriv', entry.security_level.value)
                self.assertEqual('SHA', entry.auth_protocol.value)
                self.assertEqual('authkey2', entry.auth_key.raw)
                self.assertIsNone(entry.priv_protocol)
                self.assertEqual('', entry.priv_key.raw)
            elif name == 'user-public':
                self.assertEqual('user-public', entry.name)
                self.assertEqual('SNMPv2c', entry.mode.value)
                self.assertEqual('public', entry.community.value)
            else:
                self.assertTrue(False)

    @patches.conf_data(utils.conf_full_path('access.conf'))
    def test_user_config_save_reload(self, conf_file):

        def _read_passwd(conf_file):
            with open(conf_file, 'r') as f:
                tuples = [(line.split()[5], line.split()[7])
                          for line in f.readlines()
                          if line.startswith('SNMPv3')]
            return [e for t in tuples for e in t]

        conf = config.UserConfig(conf_file)
        conf.save()
        encrypt_passwds = _read_passwd(conf_file)
        self.assertEqual(len(encrypt_passwds), 4)
        for passwd in encrypt_passwds:
            self.assertTrue(any([passwd == '-', cipher.is_encrypted(passwd)]))

        self.test_agent_config(conf_file)
