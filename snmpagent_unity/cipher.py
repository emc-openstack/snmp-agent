# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import binascii
from Crypto.Cipher import AES

__I_AM_SAFE = b'54e7818bb6534f1b'
__ENCRYPTED_FLAG = '\x06'
__MODE = AES.MODE_CBC


def is_encrypted(data):
    return data is not None and data.endswith(__ENCRYPTED_FLAG)


def encrypt(data):
    encrypted = data
    if data and not is_encrypted(data):
        cipher = AES.new(__I_AM_SAFE, __MODE, __I_AM_SAFE)
        length = 16  # data to encrypt needs to be multiple of 16
        padding = length - (len(data) % length)
        data += ('\0' * padding)
        enc = binascii.b2a_hex(cipher.encrypt(data.encode('utf-8')))
        encrypted = '{enc}{flag}'.format(enc=enc.decode('utf-8'),
                                         flag=__ENCRYPTED_FLAG)

    return encrypted


def decrypt(data):
    plain = data
    if is_encrypted(data):
        cipher = AES.new(__I_AM_SAFE, __MODE, __I_AM_SAFE)
        data = data.rstrip(__ENCRYPTED_FLAG)
        plain = cipher.decrypt(binascii.a2b_hex(data))
        plain = plain.rstrip(b'\0').decode('utf-8')

    return plain
