# Keylib

[![CircleCI](https://img.shields.io/circleci/project/blockstack/keylib-py/master.svg)](https://circleci.com/gh/blockstack/keylib-py/tree/master)
[![PyPI](https://img.shields.io/pypi/v/keylib.svg)](https://pypi.python.org/pypi/keylib/)
[![PyPI](https://img.shields.io/pypi/l/keylib.svg)](https://github.com/namesystem/keylib/blob/master/LICENSE)
[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

## Installation

```bash
$ pip install keylib
```

## Usage

### Private Keys

```python
>>> from keylib import ECPrivateKey
```

#### New Private Keys

```python
>>> private_key = ECPrivateKey()
>>> private_key.to_hex()
'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a01'
>>> private_key.to_wif()
'L3p8oAcQTtuokSCRHQ7i4MhjWc9zornvpJLfmg62sYpLRJF9woSu'
```

#### Imported Private Keys

```python
>>> imported_private_key = ECPrivateKey(private_key.to_hex())
>>> print private_key.to_wif() == imported_private_key.to_wif()
True
```

### Public Keys

```python
>>> from keylib import ECPublicKey
```

#### Public Keys from Private Keys

```python
>>> public_key = private_key.public_key()
>>> public_key.to_hex()
'03019979ec442e61ace8d47c6a344d791cee12d4e7bbde05fa91a62c0cda51c834'
```

#### Imported Public Keys

```python
>>> imported_public_key = ECPublicKey(public_key.to_hex())
>>> print public_key.to_hex() == imported_public_key.to_hex()
True
```

### Addresses

```python
>>> from keylib import public_key_to_address
```

#### Addresses from Public Key Objects

```python
>>> public_key.address()
'12WDrxysCBDtVxaP1n4HHj8BLqqqfaqANd'
```

#### RIPEMD160 Hashes from Public Key Objects

```python
>>> public_key.hash160()
'107eecc5868111ba06e6bd9309b2db90c555cb6e'
```

#### Addresses from Hex Public Keys

```python
>>> public_key_to_address("030589ee559348bd6a7325994f9c8eff12bd5d73cc683142bd0dd1a17abc99b0dc")
'1KbUJ4x8epz6QqxkmZbTc4f79JbWWz6g37'
```
