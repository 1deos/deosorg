import os
import json
import hashlib
import ecdsa
from binascii import hexlify, unhexlify
from ecdsa.keys import VerifyingKey
from utilitybelt import is_hex

from .hashing import bin_hash160
from .address_formatting import bin_hash160_to_address
from .key_formatting import (
    compress, decompress, encode_privkey, get_privkey_format
)
from .utils import (
    is_hex_ecdsa_pubkey, is_binary_ecdsa_pubkey, PUBLIC_KEY_MAGIC_BYTE
)


class CharEncoding():
    hex = 16
    bin = 256


class PubkeyType():
    ecdsa = 1
    uncompressed = 2
    compressed = 3


def get_public_key_format(public_key_string):
    if not isinstance(public_key_string, str):
        raise ValueError('Public key must be a string.')

    if len(public_key_string) == 64:
        return CharEncoding.bin, PubkeyType.ecdsa

    if (len(public_key_string) == 65 and
            public_key_string[0] == PUBLIC_KEY_MAGIC_BYTE):
        return CharEncoding.bin, PubkeyType.uncompressed

    if len(public_key_string) == 33:
        return CharEncoding.bin, PubkeyType.compressed

    if is_hex(public_key_string):
        if len(public_key_string) == 128:
            return CharEncoding.hex, PubkeyType.ecdsa

        if (len(public_key_string) == 130 and
                public_key_string[0:2] == hexlify(PUBLIC_KEY_MAGIC_BYTE)):
            return CharEncoding.hex, PubkeyType.uncompressed

        if len(public_key_string) == 66:
            return CharEncoding.hex, PubkeyType.compressed

    raise InvalidPublicKeyError()


def extract_bin_ecdsa_pubkey(public_key, version_byte=True):
    key_charencoding, key_type = get_public_key_format(public_key)

    if key_charencoding == CharEncoding.hex:
        bin_public_key = unhexlify(public_key)
    elif key_charencoding == CharEncoding.bin:
        bin_public_key = public_key
    else:
        raise InvalidPublicKeyError()

    if version_byte:
        if key_type == PubkeyType.ecdsa:
            return PUBLIC_KEY_MAGIC_BYTE + bin_public_key
        elif key_type == PubkeyType.uncompressed:
            return bin_public_key
        elif key_type == PubkeyType.compressed:
            return bin_public_key
        else:
            raise InvalidPublicKeyError()
    else:
        if key_type == PubkeyType.ecdsa:
            return bin_public_key
        elif key_type == PubkeyType.uncompressed:
            return bin_public_key[1:]
        elif key_type == PubkeyType.compressed:
            return decompress(bin_public_key)[1:]
        else:
            raise InvalidPublicKeyError()


def public_key_to_address(public_key, version_byte=0):
    key_charencoding, key_type = get_public_key_format(public_key)
    bin_public_key = extract_bin_ecdsa_pubkey(public_key)

    if key_type == PubkeyType.compressed:
        bin_public_key = compress(bin_public_key)

    public_key_bin_hash160 = bin_hash160(bin_public_key)

    return bin_hash160_to_address(
        public_key_bin_hash160, version_byte=version_byte)

