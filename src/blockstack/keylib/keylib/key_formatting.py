import os
import re
import sys
import time
import hmac
import base64
import hashlib
import binascii

is_python2 = sys.version_info.major == 2
is_python3 = sys.version_info.major == 3

# Elliptic curve parameters (secp256k1)
secp256k1 = {
    "P": 2**256 - 2**32 - 977,
    "N": 115792089237316195423570985008687907852837564279074904382605163141518161494337,
    "A": 0,
    "B": 7,
    "Gx": 55066263022277343669578718895168534326250603453777594175500187360389116729240,
    "Gy": 32670510020758816978083085130507043184471273380659243275938904335757337482424,
}


if is_python3:
    string_types = (str)
    string_or_bytes_types = (str, bytes)
    int_types = (int, float)

    # Base switching
    code_strings = {
        2: '01',
        10: '0123456789',
        16: '0123456789abcdef',
        32: 'abcdefghijklmnopqrstuvwxyz234567',
        58: '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
        256: ''.join([chr(x) for x in range(256)])
    }

    def bin_dbl_sha256(s):
        bytes_to_hash = from_string_to_bytes(s)
        return hashlib.sha256(hashlib.sha256(bytes_to_hash).digest()).digest()

    def lpad(msg, symbol, length):
        if len(msg) >= length:
            return msg
        return symbol * (length - len(msg)) + msg

    def get_code_string(base):
        if base in code_strings:
            return code_strings[base]
        else:
            raise ValueError("Invalid base!")

    def changebase(string, frm, to, minlen=0):
        if frm == to:
            return lpad(string, get_code_string(frm)[0], minlen)
        return encode(decode(string, frm), to, minlen)

    def bin_to_b58check(inp, magicbyte=0):
        inp_fmtd = from_int_to_byte(int(magicbyte))+inp

        leadingzbytes = 0
        for x in inp_fmtd:
            if x != 0:
                break
            leadingzbytes += 1

        checksum = bin_dbl_sha256(inp_fmtd)[:4]
        return '1' * leadingzbytes + changebase(inp_fmtd+checksum, 256, 58)

    def bytes_to_hex_string(b):
        if isinstance(b, str):
            return b

        return ''.join('{:02x}'.format(y) for y in b)

    def safe_from_hex(s):
        return bytes.fromhex(s)

    def from_int_representation_to_bytes(a):
        return bytes(str(a), 'utf-8')

    def from_int_to_byte(a):
        return bytes([a])

    def from_byte_to_int(a):
        return a

    def from_string_to_bytes(a):
        return a if isinstance(a, bytes) else bytes(a, 'utf-8')

    def safe_hexlify(a):
        return str(binascii.hexlify(a), 'utf-8')

    def encode(val, base, minlen=0):
        base, minlen = int(base), int(minlen)
        code_string = get_code_string(base)
        result_bytes = bytes()
        while val > 0:
            curcode = code_string[val % base]
            result_bytes = bytes([ord(curcode)]) + result_bytes
            val //= base

        pad_size = minlen - len(result_bytes)

        padding_element = b'\x00' if base == 256 else b'1' \
            if base == 58 else b'0'
        if (pad_size > 0):
            result_bytes = padding_element*pad_size + result_bytes

        result_string = ''.join([chr(y) for y in result_bytes])
        result = result_bytes if base == 256 else result_string

        return result

    def decode(string, base):
        if base == 256 and isinstance(string, str):
            string = bytes(bytearray.fromhex(string))
        base = int(base)
        code_string = get_code_string(base)
        result = 0
        if base == 256:
            def extract(d, cs):
                return d
        else:
            def extract(d, cs):
                return cs.find(d if isinstance(d, str) else chr(d))

        if base == 16:
            string = string.lower()
        while len(string) > 0:
            result *= base
            result += extract(string[0], code_string)
            string = string[1:]
        return result

    def random_string(x):
        return str(os.urandom(x))
else:
    string_types = (str, unicode)
    string_or_bytes_types = string_types
    int_types = (int, float, long)

    # Base switching
    code_strings = {
        2: '01',
        10: '0123456789',
        16: '0123456789abcdef',
        32: 'abcdefghijklmnopqrstuvwxyz234567',
        58: '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
        256: ''.join([chr(x) for x in range(256)])
    }

    def bin_dbl_sha256(s):
        bytes_to_hash = from_string_to_bytes(s)
        return hashlib.sha256(hashlib.sha256(bytes_to_hash).digest()).digest()

    def lpad(msg, symbol, length):
        if len(msg) >= length:
            return msg
        return symbol * (length - len(msg)) + msg

    def get_code_string(base):
        if base in code_strings:
            return code_strings[base]
        else:
            raise ValueError("Invalid base!")

    def changebase(string, frm, to, minlen=0):
        if frm == to:
            return lpad(string, get_code_string(frm)[0], minlen)
        return encode(decode(string, frm), to, minlen)

    def bin_to_b58check(inp, magicbyte=0):
        inp_fmtd = chr(int(magicbyte)) + inp
        leadingzbytes = len(re.match('^\x00*', inp_fmtd).group(0))
        checksum = bin_dbl_sha256(inp_fmtd)[:4]
        return '1' * leadingzbytes + changebase(inp_fmtd+checksum, 256, 58)

    def bytes_to_hex_string(b):
        return b.encode('hex')

    def safe_from_hex(s):
        return s.decode('hex')

    def from_int_representation_to_bytes(a):
        return str(a)

    def from_int_to_byte(a):
        return chr(a)

    def from_byte_to_int(a):
        return ord(a)

    def from_bytes_to_string(s):
        return s

    def from_string_to_bytes(a):
        return a

    def safe_hexlify(a):
        return binascii.hexlify(a)

    def encode(val, base, minlen=0):
        base, minlen = int(base), int(minlen)
        code_string = get_code_string(base)
        result = ""
        while val > 0:
            result = code_string[val % base] + result
            val //= base
        return code_string[0] * max(minlen - len(result), 0) + result

    def decode(string, base):
        base = int(base)
        code_string = get_code_string(base)
        result = 0
        if base == 16:
            string = string.lower()
        while len(string) > 0:
            result *= base
            result += code_string.find(string[0])
            string = string[1:]
        return result

    def random_string(x):
        return os.urandom(x)


def bin_dbl_sha256(s):
    bytes_to_hash = from_string_to_bytes(s)
    return hashlib.sha256(hashlib.sha256(bytes_to_hash).digest()).digest()


def b58check_to_bin(inp):
    leadingzbytes = len(re.match('^1*', inp).group(0))
    data = b'\x00' * leadingzbytes + changebase(inp, 58, 256)
    assert bin_dbl_sha256(data[:-4])[:4] == data[-4:]
    return data[1:-4]


def get_pubkey_format(pub):
    if is_python3:
        two = 2
        three = 3
        four = 4
    else:
        two = '\x02'
        three = '\x03'
        four = '\x04'

    if isinstance(pub, (tuple, list)):
        return 'decimal'
    elif len(pub) == 65 and pub[0] == four:
        return 'bin'
    elif len(pub) == 130 and pub[0:2] == '04':
        return 'hex'
    elif len(pub) == 33 and pub[0] in [two, three]:
        return 'bin_compressed'
    elif len(pub) == 66 and pub[0:2] in ['02', '03']:
        return 'hex_compressed'
    elif len(pub) == 64:
        return 'bin_electrum'
    elif len(pub) == 128:
        return 'hex_electrum'
    else:
        raise Exception("Pubkey not in recognized format")


def get_privkey_format(priv):
    if isinstance(priv, int_types):
        return 'decimal'
    elif len(priv) == 32:
        return 'bin'
    elif len(priv) == 33:
        return 'bin_compressed'
    elif len(priv) == 64:
        return 'hex'
    elif len(priv) == 66:
        return 'hex_compressed'
    else:
        bin_p = b58check_to_bin(priv)
        if len(bin_p) == 32:
            return 'wif'
        elif len(bin_p) == 33:
            return 'wif_compressed'
        else:
            raise Exception("WIF does not represent privkey")


def decode_pubkey(pub, formt=None):
    if not formt:
        formt = get_pubkey_format(pub)
    if formt == 'decimal':
        return pub
    elif formt == 'bin':
        return (decode(pub[1:33], 256), decode(pub[33:65], 256))
    elif formt == 'bin_compressed':
        x = decode(pub[1:33], 256)
        A, B, P = secp256k1['A'], secp256k1['B'], secp256k1['P']
        beta = pow(int(x*x*x+A*x+B), int((P+1)//4), int(P))
        y = (P-beta) if ((beta + from_byte_to_int(pub[0])) % 2) else beta
        return (x, y)
    elif formt == 'hex':
        return (decode(pub[2:66], 16), decode(pub[66:130], 16))
    elif formt == 'hex_compressed':
        return decode_pubkey(safe_from_hex(pub), 'bin_compressed')
    elif formt == 'bin_electrum':
        return (decode(pub[:32], 256), decode(pub[32:64], 256))
    elif formt == 'hex_electrum':
        return (decode(pub[:64], 16), decode(pub[64:128], 16))
    else:
        raise Exception("Invalid format!")


def encode_pubkey(pub, formt):
    if not isinstance(pub, (tuple, list)):
        pub = decode_pubkey(pub)
    if formt == 'decimal':
        return pub
    elif formt == 'bin':
        return b'\x04' + encode(pub[0], 256, 32) + encode(pub[1], 256, 32)
    elif formt == 'bin_compressed':
        return from_int_to_byte(2+(pub[1] % 2)) + encode(pub[0], 256, 32)
    elif formt == 'hex':
        return '04' + encode(pub[0], 16, 64) + encode(pub[1], 16, 64)
    elif formt == 'hex_compressed':
        return '0'+str(2+(pub[1] % 2)) + encode(pub[0], 16, 64)
    elif formt == 'bin_electrum':
        return encode(pub[0], 256, 32) + encode(pub[1], 256, 32)
    elif formt == 'hex_electrum':
        return encode(pub[0], 16, 64) + encode(pub[1], 16, 64)
    else:
        raise Exception("Invalid format!")


def compress(pubkey):
    f = get_pubkey_format(pubkey)
    if 'compressed' in f:
        return pubkey
    elif f == 'bin':
        return encode_pubkey(decode_pubkey(pubkey, f), 'bin_compressed')
    elif f == 'hex' or f == 'decimal':
        return encode_pubkey(decode_pubkey(pubkey, f), 'hex_compressed')


def decompress(pubkey):
    f = get_pubkey_format(pubkey)
    if 'compressed' not in f:
        return pubkey
    elif f == 'bin_compressed':
        return encode_pubkey(decode_pubkey(pubkey, f), 'bin')
    elif f == 'hex_compressed' or f == 'decimal':
        return encode_pubkey(decode_pubkey(pubkey, f), 'hex')


def decode_privkey(priv,formt=None):
    if not formt:
        formt = get_privkey_format(priv)
    if formt == 'decimal':
        return priv
    elif formt == 'bin':
        return decode(priv, 256)
    elif formt == 'bin_compressed':
        return decode(priv[:32], 256)
    elif formt == 'hex':
        return decode(priv, 16)
    elif formt == 'hex_compressed':
        return decode(priv[:64], 16)
    elif formt == 'wif':
        return decode(b58check_to_bin(priv),256)
    elif formt == 'wif_compressed':
        return decode(b58check_to_bin(priv)[:32],256)
    else:
        raise Exception("WIF does not represent privkey")


def encode_privkey(priv, formt, vbyte=0):
    if not isinstance(priv, int_types):
        return encode_privkey(decode_privkey(priv), formt, vbyte)
    if formt == 'decimal':
        return priv
    elif formt == 'bin':
        return encode(priv, 256, 32)
    elif formt == 'bin_compressed':
        return encode(priv, 256, 32)+b'\x01'
    elif formt == 'hex':
        return encode(priv, 16, 64)
    elif formt == 'hex_compressed':
        return encode(priv, 16, 64)+'01'
    elif formt == 'wif':
        return bin_to_b58check(encode(priv, 256, 32), 128+int(vbyte))
    elif formt == 'wif_compressed':
        return bin_to_b58check(encode(priv, 256, 32)+b'\x01', 128+int(vbyte))
    else:
        raise Exception("Invalid format!")

