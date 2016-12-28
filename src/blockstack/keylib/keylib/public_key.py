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
from ecdsa.keys import VerifyingKey

from .key_formatting import compress
from .exceptions import InvalidPublicKeyError
from .hashing import bin_hash160
from .b58check import b58check_encode
from .address_formatting import bin_hash160_to_address
from .public_key_encoding import (
    CharEncoding, PubkeyType, get_public_key_format, extract_bin_ecdsa_pubkey
)


class ECPublicKey():
    _curve = ecdsa.curves.SECP256k1
    _version_byte = 0

    @classmethod
    def version_byte(cls):
        return cls._version_byte

    def __init__(self, public_key_string, version_byte=None, verify=True):
        """ Takes in a public key in hex format.
        """
        # set the version byte
        if version_byte:
            self._version_byte = version_byte

        self._charencoding, self._type = get_public_key_format(
            public_key_string)

        # extract the binary bitcoin key (compressed/uncompressed w magic byte)
        self._bin_public_key = extract_bin_ecdsa_pubkey(public_key_string)

        # extract the bin ecdsa public key (uncompressed, w/out a magic byte)
        bin_ecdsa_public_key = extract_bin_ecdsa_pubkey(public_key_string, version_byte=False)
        if verify:
            try:
                # create the ecdsa key object
                self._ecdsa_public_key = VerifyingKey.from_string(
                    bin_ecdsa_public_key, self._curve)
            except AssertionError as e:
                raise InvalidPublicKeyError()

    def to_bin(self):
        return self._bin_public_key

    def to_hex(self):
        return hexlify(self.to_bin())

    def to_pem(self):
        return self._ecdsa_public_key.to_pem()

    def to_der(self):
        return hexlify(self._ecdsa_public_key.to_der())

    def bin_hash160(self):
        if not hasattr(self, '_bin_hash160'):
            binary_key = self.to_bin()  
            if self._type == PubkeyType.compressed:
                binary_key = compress(binary_key)
            self._bin_hash160 = bin_hash160(binary_key)
        return self._bin_hash160

    def hash160(self):
        return hexlify(self.bin_hash160())

    def address(self):
        return bin_hash160_to_address(
            self.bin_hash160(), version_byte=self._version_byte)
