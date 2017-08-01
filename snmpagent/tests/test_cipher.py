# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import ddt

from snmpagent import cipher


@ddt.ddt
class TestCipher(unittest.TestCase):
    def test_is_encrypted_true(self):
        data = 'abc\x06'
        self.assertTrue(cipher.is_encrypted(data))

    def test_is_encrypted_false(self):
        data = 'abc'
        self.assertFalse(cipher.is_encrypted(data))

    @ddt.data('abc', 'abcdefghijkl', 'abcdefghijklmn')
    def test_encrypt_decrypt(self, data):
        encrypted = cipher.encrypt(data)
        self.assertNotEqual(encrypted, data)

        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, data)
