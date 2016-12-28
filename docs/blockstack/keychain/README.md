# Keychain Manager

[![CircleCI](https://img.shields.io/circleci/project/blockstack/keychain-manager-py.svg)](https://pypi.python.org/pypi/keychain/)
[![PyPI](https://img.shields.io/pypi/v/keychain.svg)](https://pypi.python.org/pypi/keychain/)
[![PyPI](https://img.shields.io/pypi/dm/keychain.svg)](https://pypi.python.org/pypi/keychain/)
[![PyPI](https://img.shields.io/pypi/l/keychain.svg)](https://pypi.python.org/pypi/keychain/)
[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

A key system (implemented in python) based around hierarchical deterministic (HD / BIP32) public and private keychains, each with ECDSA keypairs and the ability to generate child keys (the ones Bitcoin uses).

### Getting Started

```
pip install keychain
```

```python
>>> from keychain import PrivateKeychain, PublicKeychain
```

### Private Keychains

*Note: A private keychain is a BIP32 hierarchical determinstic extended private key.*

```python
>>> private_keychain = PrivateKeychain("xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi")
>>> print private_keychain
xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi
>>> private_key = private_keychain.private_key()
```

### Public Keychains

*Note: A public keychain is a BIP32 hierarchical determinstic extended public key.*

#### Public Keychains from Private Keychains

```python
>>> public_keychain = private_keychain.public_keychain()
>>> print public_keychain
xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8
>>> public_key = public_keychain.public_key()
>>> address = public_keychain.address()
```

#### Public Keychains From Serialized Data

```python
>>> public_keychain = PublicKeychain("xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8")
```

#### Public Keychains from Public Keys

```python
>>> public_key = '032532502314356f83068bdbd283c86398d9ffd1308192474e6d3d6156eaf3d67f'
>>> chain_path = '\x00'*32
>>> public_keychain = PublicKeychain.from_public_key(public_key, chain_path)
```

You can also leave out the chain path like so:

```python
>>> public_keychain = PublicKeychain.from_public_key(public_key)
```

### Un-hardened Child Keychains

Un-hardened keychains use the public key as a seed to derive the child. This means that you can derive the parent public keychain of a given public keychain that was derived in an un-hardened way.

#### Private Un-hardened Child Keychains

```python
>>> private_child = private_keychain.hardened_child(0).child(1)
```

#### Public Un-hardened Child Keychains

```python
>>> public_child = private_child.public_keychain(0)
>>> public_grandchild = public_child.child(1)
```

### Hardened Child Keychains

Hardened keychains use the private key as a seed to derive the child. This means that with a public keychain derived from a hardened private keychain, you can't derive the parent public keychain, as is the case with the un-hardened counterparts.

#### Private Hardened Child Keychains

```python
>>> private_hardened_child = private_keychain.hardened_child(0)
```

#### Public Hardened Child Keychains

*Note: these do not exist, as a private key is required to harden a child.*
