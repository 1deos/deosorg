from binascii import hexlify, unhexlify
from utilitybelt import is_int, dev_random_entropy, dev_urandom_entropy, is_hex

PUBLIC_KEY_MAGIC_BYTE = '\x04'
COMPRESSED_PUBLIC_KEY_MAGIC_BYTES = ['\x02', '\x03']


def is_secret_exponent(val, curve_order):
    return (isinstance(val, (int, long)) and val >= 1 and val < curve_order)


def is_hex_ecdsa_pubkey(val):
    return (is_hex(val) and len(val) == 128)


def is_binary_ecdsa_pubkey(val):
    return (isinstance(val, str) and len(val) == 64)


def random_secret_exponent(curve_order):
    """ Generates a random secret exponent. """
    # run a rejection sampling algorithm to ensure the random int is less
    # than the curve order
    while True:
        # generate a random 256 bit hex string
        random_hex = hexlify(dev_urandom_entropy(32))
        random_int = int(random_hex, 16)
        if random_int >= 1 and random_int < curve_order:
            break
    return random_int
