# TrezorPass hardware-backed password manager

A PyQt-based password manager that uses [Trezor](http://www.bitcointrezor.com/)
hardware token to do encryption of passwords. Similar to KeepassX or
kwalletmanager in function.

Password database is stored in encrypted form on computer. This allows unlimited
count of password entries to be stored and enables possibility of recovery
if original Trezor is misplaced (mnemonic and passphrase are required to recover).

Note that this is alpha software.

Trezor must be already set up to use passphrase.

![A few stored passwords](https://i.imgur.com/lboB2T3.png)

# Security features

  * symmetric password encryption key never leaves the Trezor
  * button confirmation on Trezor is required to activate decryption of a password 
  * upon requesting password decryption, user sees on Trezor's display decryption
    of which password group is requested before confirmation
  * backup/export of passwords possible, also requires explicit button confirmation
  * if Trezor is lost, recovery from seed on a new Trezor and using the same
    password will also recover encrypted password database (in theory recovery
    can be done without Trezor, but such script is not yet written)

# Runtime requirements

  * PyCrypto
  * PyQt4
  * [trezorlib from python-trezor](https://github.com/trezor/python-trezor)

# Building

Even though the whole code is in Python, there are few Qt .ui form files that
need to be transformed into Python files. There's Makefile, you just need to run

    make

## Build requirements

PyQt4 development tools are necessary, namely `pyuic4` (look for packages named
like `pyqt4-dev-tools` or `PyQt4-devel`).

# Running

Run:

    python TrezorPass.py

# How backup works

Each password is encrypted and stored twice. Once with symmetric AES-CBC function
of Trezor that always requires button confirmation on device to decrypt. Second
encryption is done to public RSA key, whose private counterpart is encrypted
with Trezor. Backup requires private RSA to be decrypted and then used to decrypt
the passwords.
