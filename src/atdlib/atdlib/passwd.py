#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

from os import getenv

__all__ = ["PasswordMap"]

class PasswordGroup(object):
    """ Holds data for one password group.

    Each entry has three values:
    - key
    - symetrically AES-CBC encrypted password unlockable only by Trezor
    - RSA-encrypted password for creating backup of all password groups
    """

    def __init__(self):
        self.entries = []

    def addEntry(self, key, encryptedValue, backupValue):
        """ Add key-value-backud entry.
        """
        self.entries.append((key, encryptedValue, backupValue))

    def removeEntry(self, index):
        """ Remove entry at given index.
        """
        self.entries.pop(index)

    def updateEntry(self, index, key, encryptedValue, backupValue):
        """ Update pair at index w/ key, value & backup-encrypted passwd.
        """
        self.entries[index] = (key, encryptedValue, backupValue)

    def entry(self, index):
        """ Return entry with given index.
        """
        return self.entries[index]

class PasswordMap(object):
    """ Storage of groups of passwords in memory.

    On-Disk,    Format:
    - 4 bytes   header "TZPW"
    - 4 bytes   data storage version, network order uint32_t
    - 32 bytes  AES-CBC-encrypted wrappedOuterKey
    - 16 bytes  IV
    - 2 bytes   backup private key size (B)
    - B bytes   encrypted backup key
    - 4 bytes   size of data following (N)
    - N bytes   AES-CBC encrypted blob containing pickled struct for pwd map
    - 32 bytes  HMAC-SHA256 over data w/ same key as AES-CBC data struct above
    """

    BLOCKSIZE = getenv("ATDLIB_PASSWD_BLOCKSIZE", 16)
    MACSIZE = getenv("ATDLIB_PASSWD_MACSIZE", 32)
    KEYSIZE = getenv("ATDLIB_PASSWD_KEYSIZE", 32)

    def __init__(self, trezor):
        assert trezor is not None
        self.groups = {}
        self.trezor = trezor
        self.outerKey = None # outer AES-CBC key
        self.outerIv = None  # IV for data blob encrypted with outerKey
        self.backupKey = None

    def addGroup(self, groupName):
        """ Add group by name as utf-8 encoded string
        """
        self._add_group(groupName)

    def _add_group(self, groupName):
        if groupName in self.groups:
            raise KeyError("Group name already exists")
        self.groups[groupName] = DeOS_PasswordGroup()

    def load(self, fname):
        """ Load encrypted passwords from disk file, decrypt outer
        layer containing key names. Requires Trezor connected.

        @throws IOError: if reading file failed
        """
        self._load(fname)

    def _load(self, fname):
        with file(fname) as f:
            header = f.read(len(Magic.headerStr))
            if header != Magic.headerStr:
                out = "Bad header in storage file"
                raise IOError(out)

            version = f.read(4)
            if len(version) != 4 or struct.unpack("!I", version)[0] != 1:
                out = "Unknown version of storage file"
                raise IOError(out)

            wrappedKey = f.read(DeOS_VAULT_KEY_SIZE)
            if len(wrappedKey) != DeOS_VAULT_KEY_SIZE:
                out = "Corrupted disk format - bad wrapped key length"
                raise IOError(out)

            self.outerKey = self.unwrapKey(wrappedKey)
            self.outerIv = f.read(DeOS_VAULT_BLOCK_SIZE)
            if len(self.outerIv) != DeOS_VAULT_BLOCK_SIZE:
                out = "Corrupted disk format - bad IV length"
                raise IOError(out)

            lb = f.read(2)
            if len(lb) != 2:
                out = "Corrupted disk format - bad backup key length"
                raise IOError(out)

            lb = struct.unpack("!H", lb)[0]
            self.backupKey = DeOS_Backup(self.trezor)
            serializedBackup = f.read(lb)
            if len(serializedBackup) != lb:
                out = "Corrupted disk format - not enough encrypted backup key bytes"
                raise IOError(out)
            self.backupKey.deserialize(serializedBackup)

            ls = f.read(4)
            if len(ls) != 4:
                out = "Corrupted disk format - bad data length"
                raise IOError(out)

            l = struct.unpack("!I", ls)[0]
            encrypted = f.read(l)
            if len(encrypted) != l:
                out = "Corrupted disk format - not enough data bytes"
                raise IOError()

            hmacDigest = f.read(DeOS_VAULT_MAC_SIZE)
            if len(hmacDigest) != DeOS_VAULT_MAC_SIZE:
                out = "Corrupted disk format - HMAC not complete"
                raise IOError(out)

            # time-invariant HMAC comparison that also works with python 2.6
            newHmacDigest = hmac.new(self.outerKey,
                                     encrypted,
                                     hashlib.sha256).digest()
            hmacCompare = 0
            for (ch1, ch2) in zip(hmacDigest, newHmacDigest):
                hmacCompare |= int(ch1 != ch2)
            if hmacCompare != 0:
                out = "Corrupted disk format - HMAC does not match or bad passphrase"
                raise IOError(out)

            serialized = self.decryptOuter(encrypted, self.outerIv)
            self.groups = cPickle.loads(serialized)

    def save(self, fname):
        """ Write passwd db to disk, encrypt it. Requires Trezor.

        @throws IOError: if writing file failed
        """
        self._save(fname)

    def _save(self, fname):
        assert len(self.outerKey) == DeOS_VAULT_KEY_SIZE
        rnd = Random.new()
        self.outerIv = rnd.read(DeOS_VAULT_BLOCK_SIZE)
        wrappedKey = self.wrapKey(self.outerKey)
        with file(fname, "wb") as f:
            version = 1
            f.write(Magic.headerStr)
            f.write(struct.pack("!I", version))
            f.write(wrappedKey)
            f.write(self.outerIv)
            serialized = cPickle.dumps(self.groups, cPickle.HIGHEST_PROTOCOL)
            encrypted = self.encryptOuter(serialized, self.outerIv)
            hmacDigest = hmac.new(self.outerKey,
                                  encrypted,
                                  hashlib.sha256).digest()
            serializedBackup = self.backupKey.serialize()
            lb = struct.pack("!H", len(serializedBackup))
            f.write(lb)
            f.write(serializedBackup)
            l = struct.pack("!I", len(encrypted))
            f.write(l)
            f.write(encrypted)
            f.write(hmacDigest)
            f.flush()
            f.close()

    def encryptOuter(self, plaintext, iv):
        """ Pad and encrypt with self.outerKey
        """
        return self._encrypt(plaintext, iv, self.outerKey)

    def _encrypt(self, plaintext, iv, key):
        """ Pad plaintext with PKCS#5 and encrypt it.
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded = Padding(self.BLOCKSIZE).pad(plaintext)
        return cipher.encrypt(padded)

    def decryptOuter(self, ciphertext, iv):
        """ Decrypt with self.outerKey and unpad
        """
        return self._decrypt(ciphertext, iv, self.outerKey)

    def _decrypt(self, ciphertext, iv, key):
        """ Decrypt ciphertext, unpad it and return
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)
        unpadded = Padding(self.BLOCKSIZE).unpad(plaintext)
        return unpadded

    def unwrapKey(self, wrappedOuterKey):
        """ Decrypt wrapped outer key using Trezor.
        """
        return self._unwrap_key(wrappedOuterKey)

    def _unwrap_key(self, key):
        return self.trezor.decrypt_keyvalue(Magic.unlockNode,
                                            Magic.unlockKey,
                                            key,
                                            ask_on_encrypt=False,
                                            ask_on_decrypt=True)

    def wrapKey(self, keyToWrap):
        """ Encrypt/wrap a key. Its size must be multiple of 16.
        """
        return self._wrap_key(keyToWrap)

    def _wrap_key(self, key):
        return self.trezor.encrypt_keyvalue(Magic.unlockNode,
                                            Magic.unlockKey,
                                            key,
                                            ask_on_encrypt=False,
                                            ask_on_decrypt=True)

    def encryptPassword(self, password, groupName):
        """ Encrypt a password. Does PKCS#5 padding before encryption.
        Store IV as first block.

        @param groupName key that will be shown to user on Trezor and
            used to encrypt the password. A string in utf-8
        """
        return self._encrypt_password(password, groupName)

    def _encrypt_password(self, password, groupName):
        rnd = Random.new()
        rndBlock = rnd.read(self.BLOCKSIZE)
        padded = Padding(self.BLOCKSIZE).pad(password)
        ugroup = groupName.decode("utf-8")
        return rndBlock + self.trezor.encrypt_keyvalue(Magic.groupNode,
                                                       ugroup,
                                                       padded,
                                                       ask_on_encrypt=False,
                                                       ask_on_decrypt=True,
                                                       iv=rndBlock)

    def decryptPassword(self, encryptedPassword, groupName):
        """ Decrypt a password. First block is IV. After decryption
        strips PKCS#5 padding.

        @param groupName key that will be shown to user on Trezor
        and was used to encrypt the password. A string in UTF-8.
        """
        return self._decrypt_password(encryptedPassword, groupName)

    def _decrypt_password(self, encryptedPassword, groupName):
        ugroup = groupName.decode("utf-8")
        iv, encryptedPassword = encryptedPassword[:self.BLOCKSIZE],\
            encryptedPassword[self.BLOCKSIZE:]
        plain = self.trezor.decrypt_keyvalue(Magic.groupNode,
                                             ugroup,
                                             encryptedPassword,
                                             ask_on_encrypt=False,
                                             ask_on_decrypt=True,
                                             iv=iv)
        return Padding(self.BLOCKSIZE).unpad(plain)
