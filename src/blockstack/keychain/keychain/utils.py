from binascii import unhexlify


def extract_bin_chain_path(chain_path):
    if len(chain_path) == 64:
        return unhexlify(chain_path)
    elif len(chain_path) == 32:
        return chain_path
    else:
        raise ValueError('Invalid chain path')
