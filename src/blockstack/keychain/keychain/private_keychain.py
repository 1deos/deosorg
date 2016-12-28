from bitmerchant.wallet import Wallet as HDWallet
from .public_keychain import PublicKeychain
from binascii import unhexlify, hexlify
from bitcoin import (
    bip32_serialize,
    encode_privkey as encode_private_key
)
from .utils import extract_bin_chain_path
from .configs import EXTENDED_PRIVATE_KEY_VERSION_BYTES as version_bytes


class PrivateKeychain():
    def __init__(self, private_keychain=None):
        if private_keychain:
            if isinstance(private_keychain, HDWallet):
                self.hdkeychain = private_keychain
            elif isinstance(private_keychain, (str, unicode)):
                self.hdkeychain = HDWallet.deserialize(private_keychain)
            else:
                raise ValueError('private keychain must be a string')
        else:
            self.hdkeychain = HDWallet.new_random_wallet()

    def __str__(self):
        return self.hdkeychain.serialize_b58(private=True)

    def hardened_child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=True, as_private=True)
        return PrivateKeychain(child_keychain)

    def child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=False, as_private=True)
        return PrivateKeychain(child_keychain)

    def public_keychain(self):
        public_keychain = self.hdkeychain.public_copy()
        return PublicKeychain(public_keychain)

    def private_key(self, compressed=True):
        private_key = self.hdkeychain.get_private_key_hex()
        if compressed:
            private_key += '01'
        return private_key

    @classmethod
    def from_private_key(cls, private_key, chain_path='\x00'*32, depth=0,
                         fingerprint='\x00'*4, child_index=0):
        private_key_bytes = encode_private_key(private_key, 'bin_compressed')
        chain_path = extract_bin_chain_path(chain_path)
        keychain_parts = (version_bytes, depth, fingerprint,
                          child_index, chain_path, private_key_bytes)
        public_keychain_string = bip32_serialize(keychain_parts)
        return PrivateKeychain(public_keychain_string)
