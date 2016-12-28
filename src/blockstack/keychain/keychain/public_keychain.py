from bitmerchant.wallet import (
    Wallet as HDWallet
)
from bitcoin import (
    bip32_serialize,
    encode_pubkey as encode_public_key
)
from binascii import hexlify, unhexlify
from .utils import extract_bin_chain_path
from .configs import EXTENDED_PUBLIC_KEY_VERSION_BYTES as version_bytes


class PublicKeychain():
    def __init__(self, public_keychain):
        if isinstance(public_keychain, HDWallet):
            self.hdkeychain = public_keychain
        elif isinstance(public_keychain, (str, unicode)):
            self.hdkeychain = HDWallet.deserialize(public_keychain)
        else:
            raise ValueError('public keychain must be a string')

    def __str__(self):
        return self.hdkeychain.serialize_b58(private=False)

    def child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=False, as_private=False)
        return PublicKeychain(child_keychain)

    def descendant(self, chain_path):
        """ A descendant is a child many steps down.
        """
        public_child = self.hdkeychain
        chain_step_bytes = 4
        max_bits_per_step = 2**31
        chain_steps = [
            int(chain_path[i:i+chain_step_bytes*2], 16) % max_bits_per_step
            for i in range(0, len(chain_path), chain_step_bytes*2)
        ]
        for step in chain_steps:
            public_child = public_child.get_child(step)

        return PublicKeychain(public_child)

    def public_key(self, compressed=True):
        return self.hdkeychain.get_public_key_hex(compressed=compressed)

    def address(self):
        return str(self.hdkeychain.to_address())

    @classmethod
    def from_public_key(cls, public_key, chain_path='\x00'*32, depth=0,
                        fingerprint='\x00'*4, child_index=0):
        public_key_bytes = encode_public_key(public_key, 'bin_compressed')
        chain_path = extract_bin_chain_path(chain_path)
        keychain_parts = (version_bytes, depth, fingerprint,
                          child_index, chain_path, public_key_bytes)
        public_keychain_string = bip32_serialize(keychain_parts)
        return PublicKeychain(public_keychain_string)
