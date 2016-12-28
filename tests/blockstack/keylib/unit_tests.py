import json
import unittest
import traceback
from test import test_support

from keylib import (
    b58check_encode, b58check_decode, b58check_unpack,
    ECPrivateKey, ECPublicKey, public_key_to_address
)

_uncompressed_info = {
    'bin_private_key': '\xc4\xbb\xcb\x1f\xbe\xc9\x9de\xbfY\xd8\\\x8c\xb6.\xe2\xdb\x96?\x0f\xe1\x06\xf4\x83\xd9\xaf\xa7;\xd4\xe3\x9a\x8a',
    'hex_private_key': 'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a',
    'hex_public_key': '0478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455',
    'hex_hash160': 'c4c5d791fcb4654a1ef5e03fe0ad3d9c598f9827',
    'wif_private_key': '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
    'address': '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T',
    'wif_version_byte': 128,
    'pem_private_key': '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIMS7yx++yZ1lv1nYXIy2LuLblj8P4Qb0g9mvpzvU45qKoAcGBSuBBAAK\noUQDQgAEeNQwJ0+MXsEyEzgVHp8n9MZ2oAi9+GONB8C2vpqzXHGhUYBjJDrNTf6W\ntm4/LsgBPI4HLNCbODShn4H2Wcw0VQ==\n-----END EC PRIVATE KEY-----\n',
    'pem_public_key': '-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEeNQwJ0+MXsEyEzgVHp8n9MZ2oAi9+GON\nB8C2vpqzXHGhUYBjJDrNTf6Wtm4/LsgBPI4HLNCbODShn4H2Wcw0VQ==\n-----END PUBLIC KEY-----\n',
    'der_private_key': '30740201010420c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8aa00706052b8104000aa1440342000478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455',
    'der_public_key': '3056301006072a8648ce3d020106052b8104000a0342000478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455'
}

_compressed_info = {
    'bin_private_key': '\xc4\xbb\xcb\x1f\xbe\xc9\x9de\xbfY\xd8\\\x8c\xb6.\xe2\xdb\x96?\x0f\xe1\x06\xf4\x83\xd9\xaf\xa7;\xd4\xe3\x9a\x8a',
    'hex_private_key': 'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a01',
    'hex_public_key': '0378d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71',
    'hex_hash160': '79fbfc3f34e7745860d76137da68f362380c606c',
    'wif_private_key': 'L3p8oAcQTtuokSCRHQ7i4MhjWc9zornvpJLfmg62sYpLRJF9woSu',
    'address': '1C7zdTfnkzmr13HfA2vNm5SJYRK6nEKyq8',
    'wif_version_byte': 128,
    'pem_private_key': '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIMS7yx++yZ1lv1nYXIy2LuLblj8P4Qb0g9mvpzvU45qKoAcGBSuBBAAK\noUQDQgAEeNQwJ0+MXsEyEzgVHp8n9MZ2oAi9+GONB8C2vpqzXHGhUYBjJDrNTf6W\ntm4/LsgBPI4HLNCbODShn4H2Wcw0VQ==\n-----END EC PRIVATE KEY-----\n',
    'pem_public_key': '-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEeNQwJ0+MXsEyEzgVHp8n9MZ2oAi9+GON\nB8C2vpqzXHGhUYBjJDrNTf6Wtm4/LsgBPI4HLNCbODShn4H2Wcw0VQ==\n-----END PUBLIC KEY-----\n',
    'der_private_key': '30740201010420c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8aa00706052b8104000aa1440342000478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455',
    'der_public_key': '3056301006072a8648ce3d020106052b8104000a0342000478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455'
}

_compressed_info_2 = {
    'hex_public_key': '02068fd9d47283fb310e6dfb66b141dd78fbabc76d073d48cddc770ffb2bd262d7',
    'bin_public_key': '\x02\x06\x8f\xd9\xd4r\x83\xfb1\x0em\xfbf\xb1A\xddx\xfb\xab\xc7m\x07=H\xcd\xdcw\x0f\xfb+\xd2b\xd7',
    'hex_hash160': '25488b0d3bb770d6e0ef07e1f19d33ab59931dee',
    'bin_hash160': '%H\x8b\r;\xb7p\xd6\xe0\xef\x07\xe1\xf1\x9d3\xabY\x93\x1d\xee',
    'address': '14Q8uVAX29RUMvqPGXL5sg6NiwwMRFCm8C',
}

_public_key_info = {
    'hex_public_key_uncompressed': '04068fd9d47283fb310e6dfb66b141dd78fbabc76d073d48cddc770ffb2bd262d7b2832f87f683100b89c2e95314deeeacbc6409af1e36c3ae3fd8c5f2f243cfec',
    'bin_public_key_uncompressed': '\x04\x06\x8f\xd9\xd4r\x83\xfb1\x0em\xfbf\xb1A\xddx\xfb\xab\xc7m\x07=H\xcd\xdcw\x0f\xfb+\xd2b\xd7\xb2\x83/\x87\xf6\x83\x10\x0b\x89\xc2\xe9S\x14\xde\xee\xac\xbcd\t\xaf\x1e6\xc3\xae?\xd8\xc5\xf2\xf2C\xcf\xec',
    'hex_public_key_raw_ecdsa': '068fd9d47283fb310e6dfb66b141dd78fbabc76d073d48cddc770ffb2bd262d7b2832f87f683100b89c2e95314deeeacbc6409af1e36c3ae3fd8c5f2f243cfec',
    'bin_public_key_raw_ecdsa': '\x06\x8f\xd9\xd4r\x83\xfb1\x0em\xfbf\xb1A\xddx\xfb\xab\xc7m\x07=H\xcd\xdcw\x0f\xfb+\xd2b\xd7\xb2\x83/\x87\xf6\x83\x10\x0b\x89\xc2\xe9S\x14\xde\xee\xac\xbcd\t\xaf\x1e6\xc3\xae?\xd8\xc5\xf2\xf2C\xcf\xec',
    'hex_public_key_compressed': '02068fd9d47283fb310e6dfb66b141dd78fbabc76d073d48cddc770ffb2bd262d7',
    'bin_public_key_compressed': '\x02\x06\x8f\xd9\xd4r\x83\xfb1\x0em\xfbf\xb1A\xddx\xfb\xab\xc7m\x07=H\xcd\xdcw\x0f\xfb+\xd2b\xd7'
}

_address_info = {
    'compressed_public_key': '030589ee559348bd6a7325994f9c8eff12bd5d73cc683142bd0dd1a17abc99b0dc',
    'compressed_address': '1KbUJ4x8epz6QqxkmZbTc4f79JbWWz6g37',
    'uncompressed_public_key': '0479BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8',
    'uncompressed_address': '1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm'
}


class ECPrivateKeyUncompressedTest(unittest.TestCase):
    ref = _uncompressed_info

    def setUp(self):
        self.private_key = ECPrivateKey(
            self.ref['hex_private_key'], compressed=False)

    def tearDown(self):
        pass

    def test_random_private_key(self):
        private_key = ECPrivateKey()
        self.assertTrue(isinstance(private_key, ECPrivateKey))

    def test_hex_private_key(self):
        self.assertEqual(self.private_key.to_hex(), self.ref['hex_private_key'])

    def test_wif_private_key(self):
        self.assertEqual(self.private_key.to_wif(), self.ref['wif_private_key'])

    def test_pem_private_key(self):
        self.assertEqual(self.private_key.to_pem(), self.ref['pem_private_key'])

    def test_der_private_key(self):
        self.assertEqual(self.private_key.to_der(), self.ref['der_private_key'])

    def test_to_public_key_conversion(self):
        public_key = self.private_key.public_key()
        self.assertEqual(public_key.to_hex(), self.ref['hex_public_key'])
        self.assertEqual(public_key.address(), self.ref['address'])


class ECPrivateKeyCompressedTest(unittest.TestCase):
    ref = _compressed_info

    def setUp(self):
        self.private_key = ECPrivateKey(
            self.ref['hex_private_key'], compressed=True)

    def tearDown(self):
        pass

    def test_random_private_key(self):
        private_key = ECPrivateKey()
        self.assertTrue(isinstance(private_key, ECPrivateKey))

    def test_hex_private_key(self):
        self.assertEqual(self.private_key.to_hex(), self.ref['hex_private_key'])

    def test_wif_private_key(self):
        self.assertEqual(self.private_key.to_wif(), self.ref['wif_private_key'])

    def test_pem_private_key(self):
        self.assertEqual(self.private_key.to_pem(), self.ref['pem_private_key'])

    def test_der_private_key(self):
        self.assertEqual(self.private_key.to_der(), self.ref['der_private_key'])

    def test_to_public_key_conversion(self):
        public_key = self.private_key.public_key()
        self.assertEqual(public_key.to_hex(), self.ref['hex_public_key'])
        self.assertEqual(public_key.address(), self.ref['address'])


class ECPrivateKeyFromWIF(unittest.TestCase):
    ref = _uncompressed_info

    def setUp(self):
        self.private_key = ECPrivateKey(
            self.ref['wif_private_key'], compressed=False)
        self.assertEqual(self.private_key_from_wif.to_hex(), self.ref['hex_private_key'])


class ECPublicKeyCreationTest(unittest.TestCase):
    ref = _public_key_info

    def setUp(self):
        self.address_compressed = '14Q8uVAX29RUMvqPGXL5sg6NiwwMRFCm8C'
        self.address_uncompressed = '1AuZor1RVzG22wqbH2sG2j5WRDZsbw1tip'

    def tearDown(self):
        pass

    def test_create_pubkey_from_hex_uncompressed_format(self):
        public_key_string = self.ref['hex_public_key_uncompressed']
        self.assertEqual(self.address_uncompressed, ECPublicKey(
            public_key_string).address())

    def test_create_pubkey_from_bin_uncompressed_format(self):
        public_key_string = self.ref['bin_public_key_uncompressed']
        self.assertEqual(self.address_uncompressed, ECPublicKey(
            public_key_string).address())

    def test_create_pubkey_from_hex_ecdsa_format(self):
        public_key_string = self.ref['hex_public_key_raw_ecdsa']
        self.assertEqual(self.address_uncompressed, ECPublicKey(
            public_key_string).address())

    def test_create_pubkey_from_bin_ecdsa_format(self):
        public_key_string = self.ref['bin_public_key_raw_ecdsa']
        self.assertEqual(self.address_uncompressed, ECPublicKey(
            public_key_string).address())

    def test_create_pubkey_from_hex_compressed_format(self):
        public_key_string = self.ref['hex_public_key_compressed']
        self.assertEqual(self.address_compressed, ECPublicKey(
            public_key_string).address())

    def test_create_pubkey_from_bin_compressed_format(self):
        public_key_string = self.ref['bin_public_key_compressed']
        self.assertEqual(self.address_compressed, ECPublicKey(
            public_key_string).address())


class BitcoinUncompressedPublicKeyTest(unittest.TestCase):
    ref = _uncompressed_info

    def setUp(self):
        self.public_key = ECPublicKey(self.ref['hex_public_key'])

    def tearDown(self):
        pass

    def test_address(self):
        self.assertEqual(self.public_key.address(), self.ref['address'])

    def test_hex_hash160(self):
        self.assertEqual(self.public_key.hash160(), self.ref['hex_hash160'])

    def test_hex_public_key(self):
        self.assertEqual(self.public_key.to_hex(), self.ref['hex_public_key'])

    def test_pem_public_key(self):
        self.assertEqual(self.public_key.to_pem(), self.ref['pem_public_key'])

    def test_der_public_key(self):
        self.assertEqual(self.public_key.to_der(), self.ref['der_public_key'])


class BitcoinCompressedPublicKeyTest(unittest.TestCase):
    def setUp(self):
        self.ref = _compressed_info_2
        self.public_key = ECPublicKey(self.ref['hex_public_key'])

    def tearDown(self):
        pass

    def test_address(self):
        self.assertEqual(self.public_key.address(), self.ref['address'])

    def test_bin_hash160(self):
        self.assertEqual(self.public_key.bin_hash160(), self.ref['bin_hash160'])

    def test_hex_hash160(self):
        self.assertEqual(self.public_key.hash160(), self.ref['hex_hash160'])

    def test_bin_public_key(self):
        self.assertEqual(self.public_key.to_bin(), self.ref['bin_public_key'])

    def test_hex_public_key(self):
        self.assertEqual(self.public_key.to_hex(), self.ref['hex_public_key'])


class BitcoinB58CheckTest(unittest.TestCase):
    ref = _uncompressed_info

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_b58check_encode_then_decode(self):
        bin_private_key = self.ref['hex_private_key'].decode('hex')
        wif_private_key = b58check_encode(
            bin_private_key, version_byte=self.ref['wif_version_byte'])
        self.assertEqual(self.ref['wif_private_key'], wif_private_key)
        bin_private_key_verification = b58check_decode(wif_private_key)
        self.assertEqual(bin_private_key_verification, bin_private_key)

    def test_b58check_unpack_then_encode(self):
        version_byte, bin_private_key, checksum = b58check_unpack(
            self.ref['wif_private_key'])
        self.assertTrue(ord(version_byte) == self.ref['wif_version_byte'])
        wif_private_key = b58check_encode(
            bin_private_key, version_byte=ord(version_byte))
        self.assertEqual(self.ref['wif_private_key'], wif_private_key)


class AddressCheckTest(unittest.TestCase):
    ref = _address_info

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_public_key_to_address_compressed(self):
        address = public_key_to_address(self.ref['compressed_public_key'])
        self.assertEqual(address, self.ref['compressed_address'])

    def test_public_key_to_address_uncompressed(self):
        address = public_key_to_address(self.ref['uncompressed_public_key'])
        self.assertEqual(address, self.ref['uncompressed_address'])


def test_main():
    test_support.run_unittest(
        ECPrivateKeyUncompressedTest,
        ECPrivateKeyCompressedTest,
        ECPrivateKeyFromWIF,
        ECPublicKeyCreationTest,
        BitcoinUncompressedPublicKeyTest,
        BitcoinCompressedPublicKeyTest,
        BitcoinB58CheckTest,
        AddressCheckTest
    )

if __name__ == '__main__':
    test_main()
