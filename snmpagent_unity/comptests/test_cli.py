import unittest
from snmpagent_unity.comptests import cli_helper

import os
import shutil
import tempfile


class SNMPCliTest(unittest.TestCase):
    def setUp(self):
        self.helper = cli_helper.Helper(conf_file=None)
        self.helper.clear_access_data()

    def test_add_user(self):
        r = self.helper.add_user('for_test', "MD5", 'password', "DES",
                                 'password')
        self.assertEqual(0, r)

    def test_update_user(self):
        self.helper.add_user('for_update', 'SHA', 'password', 'AES',
                             'password')
        r = self.helper.update_user('for_update', 'MD5', 'password1')
        self.assertEqual(0, r)

    def test_delete_user(self):
        self.helper.add_user('for_delete', 'SHA', 'password', 'AES',
                             'password')
        r = self.helper.delete_user('for_delete')
        self.assertEqual(0, r)

    def test_create_community(self):
        r = self.helper.create_community('new_user')
        self.assertEqual(0, r)

    def test_create_community_already_exists(self):
        self.helper.create_community('first')
        r = self.helper.create_community('first')
        self.assertNotEqual(0, r)

    def test_delete_community(self):
        self.helper.create_community('to_delete')
        r = self.helper.delete_community('to_delete')
        self.assertEqual(0, r)

    def test_list_users(self):
        self.helper.create_community('dummy_1')
        self.helper.create_community('dummy_2')
        r = self.helper.list_users()
        self.assertEqual(0, r)

    def test_encrypt(self):
        r, _ = self._create_encrypt_file()
        self.assertEqual(0, r)

    def _create_encrypt_file(self):
        tmp_dir = tempfile.mkdtemp(prefix=self._testMethodName)
        self.addCleanup(shutil.rmtree, tmp_dir)
        tmp_file = os.path.join(tmp_dir, 'agent.conf')
        shutil.copy(self.helper.conf_file, tmp_file)
        return self.helper.encrypt(tmp_file), tmp_file

    def test_decrypt(self):
        _, tmp_file = self._create_encrypt_file()
        self.helper.decrypt(tmp_file)

    def test_start_service(self):
        self.helper.create_community('for_start')
        r = self.helper.start_service()
        self.assertEqual(0, r)
        self.addCleanup(self.helper.stop_service)

    def test_stop_service(self):
        self.helper.create_community('for_stop')
        self.helper.start_service()
        r = self.helper.stop_service()
        self.assertEqual(0, r)

    def test_stop_service_already_stopped(self):
        r = self.helper.stop_service()
        self.assertNotEqual(0, r)

    def test_restart_service(self):
        self.helper.create_community('for_restart')
        self.helper.start_service()
        r = self.helper.restart_service()
        self.assertEqual(0, r)

    def test_restart_service_no_running(self):
        r = self.helper.restart_service()
        self.assertEqual(3, r)
