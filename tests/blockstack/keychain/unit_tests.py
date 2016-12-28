import json
import traceback
import unittest
from test import test_support
from keychain import PrivateKeychain, PublicKeychain
from bitcoin import bip32_deserialize, privkey_to_pubkey


class BasicKeychainTest(unittest.TestCase):
    def setUp(self):
        self.private_keychains = {
            "root": "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi",
            "0H": "xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6KCesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7",
            "0H/1": "xprv9wTYmMFdV23N2TdNG573QoEsfRrWKQgWeibmLntzniatZvR9BmLnvSxqu53Kw1UmYPxLgboyZQaXwTCg8MSY3H2EU4pWcQDnRnrVA1xe8fs",
            "0H/1/2H": "xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3ryjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM",
            "0H/1/2H/2": "xprvA2JDeKCSNNZky6uBCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334",
            "0H/1/2H/2/1000000000": "xprvA41z7zogVVwxVSgdKUHDy1SKmdb533PjDz7J6N6mV6uS3ze1ai8FHa8kmHScGpWmj4WggLyQjgPie1rFSruoUihUZREPSL39UNdE3BBDu76"
        }
        self.public_keychains = {
            "root": "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8",
            "0H": "xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw",
            "0H/1": "xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ",
            "0H/1/2H": "xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dFDFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5",
            "0H/1/2H/2": "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV",
            "0H/1/2H/2/1000000000": "xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaFcxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy"
        }
        self.root_private_keychain = PrivateKeychain(self.private_keychains["root"])

    def tearDown(self):
        pass

    def test_root_private_to_public(self):
        public_keychain = self.root_private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["root"]))

    def test_hardened_child_0H(self):
        private_keychain = self.root_private_keychain.hardened_child(0)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H"]))
        self.assertEqual(str(private_keychain.public_keychain()), str(self.public_keychains["0H"]))

    def test_unhardened_child_0H_1(self):
        private_keychain = self.root_private_keychain.hardened_child(0).child(1)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H/1"]))
        public_keychain = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["0H/1"]))
        public_keychain_2 = self.root_private_keychain.hardened_child(0).public_keychain().child(1)
        self.assertEqual(str(public_keychain), str(public_keychain_2))

    def test_5_step_derivation(self):
        private_keychain = self.root_private_keychain.hardened_child(0).child(1).hardened_child(2).child(2).child(1000000000)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H/1/2H/2/1000000000"]))
        public_keychain = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["0H/1/2H/2/1000000000"]))

    def test_private_key(self):
        root_private_key = self.root_private_keychain.private_key()
        self.assertTrue(len(root_private_key) == 66)

    def test_address(self):
        address = self.root_private_keychain.public_keychain().address()
        self.assertTrue(address[0] == '1')


class KeychainDescendantTest(unittest.TestCase):
    def setUp(self):
        self.public_keychain_string = 'xpub661MyMwAqRbcFQVrQr4Q4kPjaP4JjWaf39fBVKjPdK6oGBayE46GAmKzo5UDPQdLSM9DufZiP8eauy56XNuHicBySvZp7J5wsyQVpi2axzZ'
        self.public_keychain = PublicKeychain(self.public_keychain_string)
        self.chain_path = 'bd62885ec3f0e3838043115f4ce25eedd22cc86711803fb0c19601eeef185e39'
        self.reference_public_key = '03fdd57adec3d438ea237fe46b33ee1e016eda6b585c3e27ea66686c2ea5358479'

    def tearDown(self):
        pass

    def test_descendant(self):
        descendant_public_keychain = self.public_keychain.descendant(self.chain_path)
        descendant_public_key = descendant_public_keychain.public_key()
        self.assertEqual(descendant_public_key, self.reference_public_key)


class KeychainDerivationTest(unittest.TestCase):
    def setUp(self):
        self.chain_path = 'bd62885ec3f0e3838043115f4ce25eedd22cc86711803fb0c19601eeef185e39'
        self.public_key_hex = '032532502314356f83068bdbd283c86398d9ffd1308192474e6d3d6156eaf3d67f'
        self.private_key_hex = 'e4557e22988ab073d4c605c4548577a3c87019198e514346c26c3cff5d546f7e01'
        self.reference_public_keychain = 'xpub661MyMwAqRbcEYS8w7XLSVeEsBXy79zSzH1J8vCdxAZningWLdN3zgtU6SJRqgVDtiwxFwbqpq3DhkYnpKaV7ShnnpTQTmQbf1gBWB5yEhw'
        self.reference_child_0_chaincode = 'y1N\x14\x1b\xbcZ\xfe;\x88\x96\xd4\xd8@(\xe8\xc3\xd6\x9fK\x1c\x04\xa6\t\xe6%\xadz\xefcB!'

        self.private_key_hex_2 = '0e1f04e0c9154cd880b4df17357516736d53d4d1a9875ae40643b3197dfb738c'
        self.public_key_hex_2 = '04ed34a7f541de185fdcbf8e1a9f169b6a9146b62b34172cbfce22c0667b58e795bc28b30b931713743260390da739584eca6729af0e8011be4e5e7fb42b13c4c9'
        self.reference_public_keychain_2 = 'xpub661MyMwAqRbcEYS8w7XLSVeEsBXy79zSzH1J8vCdxAZningWLdN3zgtU6TpWofxjzJQxPqLwhMi3YenYyEXtWUa55DzZZCyuZzjrrusaHDJ'

        self.public_key_hex_3 = '047c7f6d1f71780ccd373a7d2a020a1aeb7d47639e86fe951f5ba23a9ca8d6f7cfb03ed7ca411b22fa5244b9998d27d9c7bf7f0603f1997d1c7b3dc5a9b342c554'

    def tearDown(self):
        pass

    def test_derivation_from_raw_keys(self):
        public_keychain = PublicKeychain.from_public_key(self.public_key_hex)
        private_keychain = PrivateKeychain.from_private_key(self.private_key_hex)
        public_keychain_2 = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(public_keychain_2))
        self.assertEqual(str(public_keychain), self.reference_public_keychain)

    def test_derivation_from_raw_uncompressed_keys(self):
        public_keychain = PublicKeychain.from_public_key(self.public_key_hex_2)
        private_keychain = PrivateKeychain.from_private_key(self.private_key_hex_2)
        public_keychain_2 = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(public_keychain_2))
        self.assertEqual(str(public_keychain), self.reference_public_keychain_2)

    def test_child_generation(self):
        public_keychain = PublicKeychain.from_public_key(self.public_key_hex)
        public_keychain_child = public_keychain.child(0)
        keychain_parts = bip32_deserialize(str(public_keychain_child))
        self.assertEqual(keychain_parts[4], self.reference_child_0_chaincode)


class HighVolumeKeyDerivationTest(unittest.TestCase):
    def setUp(self):
        self.public_key_hex = '032532502314356f83068bdbd283c86398d9ffd1308192474e6d3d6156eaf3d67f'
        self.private_key_hex = 'e4557e22988ab073d4c605c4548577a3c87019198e514346c26c3cff5d546f7e01'

    def tearDown(self):
        pass

    def test_high_volume_derivation(self):
        number_of_keys = 10
        public_keychain = PublicKeychain.from_public_key(self.public_key_hex)
        private_keychain = PrivateKeychain.from_private_key(self.private_key_hex)
        keypairs = []
        print ""
        for i in range(number_of_keys):
            print "making key %i of %i" % (i+1, number_of_keys)
            public_key = public_keychain.child(i).public_key()
            private_key = private_keychain.child(i).private_key()
            keypairs.append({ 'public': public_key, 'private': private_key })

        for i in range(len(keypairs)):
            keypair = keypairs[i]
            print "checking key %i of %i" % (i+1, number_of_keys)
            self.assertEqual(privkey_to_pubkey(keypair['private']), keypair['public'])


def test_main():
    test_support.run_unittest(
        KeychainDerivationTest,
        BasicKeychainTest,
        KeychainDescendantTest,
        HighVolumeKeyDerivationTest
    )


if __name__ == '__main__':
    test_main()