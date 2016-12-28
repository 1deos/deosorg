# -*- coding: utf-8 -*-
"""
    pybitcoin
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""

import os
import json
import hashlib
import ecdsa
from binascii import hexlify, unhexlify
from ecdsa.keys import SigningKey

from .key_formatting import compress, encode_privkey, get_privkey_format
from .b58check import b58check_encode, b58check_decode
from .public_key import ECPublicKey
from .utils import (
    random_secret_exponent, is_secret_exponent, PUBLIC_KEY_MAGIC_BYTE
)


class ECPrivateKey():
    _curve = ecdsa.curves.SECP256k1
    _hash_function = hashlib.sha256
    _pubkeyhash_version_byte = 0

    def __init__(self, private_key=None, compressed=True):
        """ Takes in a private key/secret exponent.
        """
        self._compressed = compressed
        if not private_key:
            secret_exponent = random_secret_exponent(self._curve.order)
        else:
            secret_exponent = encode_privkey(private_key, 'decimal')

        # make sure that: 1 <= secret_exponent < curve_order
        if not is_secret_exponent(secret_exponent, self._curve.order):
            raise IndexError(
                ("Secret exponent is outside of the valid range."
                 "Must be >= 1 and < the curve order."))

        self._ecdsa_private_key = ecdsa.keys.SigningKey.from_secret_exponent(
            secret_exponent, self._curve, self._hash_function
        )

    @classmethod
    def wif_version_byte(cls):
        if hasattr(cls, '_wif_version_byte'):
            return cls._wif_version_byte
        return (cls._pubkeyhash_version_byte + 128) % 256

    def to_bin(self):
        if self._compressed:
            return encode_privkey(
                self._ecdsa_private_key.to_string(), 'bin_compressed')
        else:
            return self._ecdsa_private_key.to_string()

    def to_hex(self):
        if self._compressed:
            return encode_privkey(
                self._ecdsa_private_key.to_string(), 'hex_compressed')
        else:
            return hexlify(self.to_bin())

    def to_wif(self):
        if self._compressed:
            return encode_privkey(
                self._ecdsa_private_key.to_string(), 'wif_compressed')
        else:
            return b58check_encode(
                self.to_bin(), version_byte=self.wif_version_byte())

    def to_pem(self):
        return self._ecdsa_private_key.to_pem()

    def to_der(self):
        return hexlify(self._ecdsa_private_key.to_der())

    def public_key(self):
        # lazily calculate and set the public key
        if not hasattr(self, '_public_key'):
            ecdsa_public_key = self._ecdsa_private_key.get_verifying_key()

            bin_public_key_string = "%s%s" % (
                PUBLIC_KEY_MAGIC_BYTE, ecdsa_public_key.to_string())

            if self._compressed:
                bin_public_key_string = compress(bin_public_key_string)

            # create the public key object from the public key string
            self._public_key = ECPublicKey(
                bin_public_key_string,
                version_byte=self._pubkeyhash_version_byte)

        # return the public key object
        return self._public_key
