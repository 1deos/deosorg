#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import cPickle
import hashlib
import hmac
import os
import struct
import sys
import configobj
import simplejson as json
import ruamel.yaml as yaml

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from PyQt4 import QtCore
from PyQt4 import QtGui
from trezorlib.client import BaseClient
from trezorlib.client import ProtocolMixin
from trezorlib.transport_hid import HidTransport
from trezorlib import messages_pb2

DeOS_VAULT_RSA_KEY_SIZE = 2048
DeOS_VAULT_SYMMETRIC_KEY_SIZE = 32
DeOS_VAULT_KEY_SIZE = 32
DeOS_VAULT_BLOCK_SIZE = 16
DeOS_VAULT_MAC_SIZE = 32
DeOS_VAULT_KEY_INDEX = 0 # column where key is shown in password table
DeOS_VAULT_PASSWD_INDEX = 1 # column where password is shown in password table
# column of QWidgetItem in whose data we cache decrypted passwords
DeOS_VAULT_CACHE_INDEX = 0
DeOS_VAULT_WINDOW_TITLE = "Vault"

def q2s(s):
    """
    Convert QString to UTF-8 string object
    """
    return str(s.toUtf8())

def s2q(s):
    """
    Convert UTF-8 encoded string to QString
    """
    return QtCore.QString.fromUtf8(s)

class Magic(object):
    u = lambda fmt, s: struct.unpack(fmt, s)[0]
    headerStr = 'TZPW'
    hdr = u('!I', headerStr)
    unlockNode = [hdr, u('!I', 'ULCK')] # for unlocking wrapped AES-CBC key.
    # for generating keys for individual password groups.
    groupNode = [hdr, u('!I', 'GRUP')]
    # the unlock & backup keys are written this way to fit display nicely.
    unlockKey = 'Decrypt master  key?' # string to derive wrapping key from.
    # for unlocking wrapped backup private RSA key.
    backupNode = [hdr, u('!I', 'BKUP')]
    # string to derive backup wrapping key from.
    backupKey  = 'Decrypt backup  key?'

class Padding(object):
    """
    PKCS#7 Padding for block cipher having 16-byte blocks
    """

    def __init__(self, blocksize):
        self.blocksize = blocksize

    def pad(self, s):
        BS = self.blocksize
        return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    def unpad(self, s):
        return s[0:-ord(s[-1])]

class DeOS_Backup(object):
    """
    Performs backup and restore for password storage.
    """

    RSA_KEYSIZE = DeOS_VAULT_RSA_KEY_SIZE
    SYMMETRIC_KEYSIZE = DeOS_VAULT_SYMMETRIC_KEY_SIZE
    BLOCKSIZE = DeOS_VAULT_BLOCK_SIZE

    def __init__(self, trezor):
        """
        Create with no keys prepared.

        @param trezor: client object used to encrypt private key
        """
        self.trezor = trezor
        self.publicKey = None
        self.encryptedPrivate = None # encrypted private key.
        # ephemeral key used to encrypt private RSA key.
        self.encryptedEphemeral = None
        # IV used to encrypt private key with ephemeral key.
        self.ephemeralIv = None

    def generate(self):
        """
        Generate key and encrypt private key.
        """
        key = RSA.generate(self.RSA_KEYSIZE)
        privateDer = key.exportKey(format="DER")
        self.publicKey = key.publickey()
        self.wrapPrivateKey(privateDer)

    def wrapPrivateKey(self, privateKey):
        """
        Wrap serialized private key by encrypting it with trezor.
        """
        # Trezor client won't allow to encrypt whole serialized RSA key
        # in one go - it's too big. We need an ephemeral symmetric key
        # and encrypt the small ephemeral with Trezor.
        rng = Random.new()
        ephemeral = rng.read(self.SYMMETRIC_KEYSIZE)
        self.ephemeralIv = rng.read(self.BLOCKSIZE)
        cipher = AES.new(ephemeral, AES.MODE_CBC, self.ephemeralIv)
        padded = Padding(self.BLOCKSIZE).pad(privateKey)
        self.encryptedPrivate = cipher.encrypt(padded)
        self.encryptedEphemeral = self.trezor.encrypt_keyvalue(
            Magic.backupNode, Magic.backupKey, ephemeral,
            ask_on_encrypt=False, ask_on_decrypt=True)

    def unwrapPrivateKey(self):
        """
        Decrypt private RSA key using self.encryptedEphemeral from
        self.encryptedPrivate. Encrypted ephemeral key will be
        decrypted with Trezor.

        @returns RSA private key as Crypto.RSA._RSAobj
        """
        ephemeral = self.trezor.decrypt_keyvalue(Magic.backupNode,
                                                 Magic.backupKey,
                                                 self.encryptedEphemeral,
                                                 ask_on_encrypt=False,
                                                 ask_on_decrypt=True)
        cipher = AES.new(ephemeral, AES.MODE_CBC, self.ephemeralIv)
        padded = cipher.decrypt(self.encryptedPrivate)
        privateDer = Padding(self.BLOCKSIZE).unpad(padded)
        privateKey = RSA.importKey(privateDer)
        return privateKey

    def serialize(self):
        """
        Return object data as serialized string.
        """
        publicDer = self.publicKey.exportKey(format="DER")
        picklable = (self.ephemeralIv,
                     self.encryptedEphemeral,
                     self.encryptedPrivate,
                     publicDer)
        return cPickle.dumps(picklable, cPickle.HIGHEST_PROTOCOL)

    def deserialize(self, serialized):
        """
        Set object data from serialized string
        """
        unpickled = cPickle.loads(serialized)
        (self.ephemeralIv,
            self.encryptedEphemeral,
            self.encryptedPrivate,
            publicDer) = unpickled
        self.publicKey = RSA.importKey(publicDer)

    def encryptPassword(self, password):
        """
        Encrypt password with RSA under OAEP padding and return it.
        Password must be shorter than modulus length minus padding
        length.
        """
        cipher = PKCS1_OAEP.new(self.publicKey)
        encrypted = cipher.encrypt(password)
        return encrypted

    def decryptPassword(self, encryptedPassword, privateKey):
        """
        Decrypt RSA-OAEP encrypted password.
        """
        cipher = PKCS1_OAEP.new(privateKey)
        password = cipher.decrypt(encryptedPassword)
        return password

class DeOS_PasswordGroup(object):
    """
    Holds data for one password group.

    Each entry has three values:
    - key
    - symetrically AES-CBC encrypted password unlockable only by Trezor
    - RSA-encrypted password for creating backup of all password groups
    """

    def __init__(self):
        self.entries = []

    def addEntry(self, key, encryptedValue, backupValue):
        """
        Add key-value-backud entry.
        """
        self.entries.append((key, encryptedValue, backupValue))

    def removeEntry(self, index):
        """
        Remove entry at given index.
        """
        self.entries.pop(index)

    def updateEntry(self, index, key, encryptedValue, backupValue):
        """
        Update pair at index with given key, value, and
        backup-encrypted password.
        """
        self.entries[index] = (key, encryptedValue, backupValue)

    def entry(self, index):
        """
        Return entry with given index.
        """
        return self.entries[index]

class DeOS_PasswordMap(object):
    """
    Storage of groups of passwords in memory.
    """

    BLOCKSIZE = DeOS_VAULT_BLOCK_SIZE
    MACSIZE = DeOS_VAULT_MAC_SIZE
    KEYSIZE = DeOS_VAULT_KEY_SIZE

    ## On-disk format
    #  4 bytes  header "TZPW"
    #  4 bytes  data storage version, network order uint32_t
    # 32 bytes  AES-CBC-encrypted wrappedOuterKey
    # 16 bytes  IV
    #  2 bytes  backup private key size (B)
    #  B bytes  encrypted backup key
    #  4 bytes  size of data following (N)
    #  N bytes  AES-CBC encrypted blob containing pickled struct for pwd map
    # 32 bytes  HMAC-SHA256 over data w/ same key as AES-CBC data struct above

    def __init__(self, trezor):
        assert trezor is not None
        self.groups = {}
        self.trezor = trezor
        self.outerKey = None # outer AES-CBC key
        self.outerIv = None  # IV for data blob encrypted with outerKey
        self.backupKey = None

    def addGroup(self, groupName):
        """
        Add group by name as utf-8 encoded string
        """
        self._add_group(groupName)

    def _add_group(self, groupName):
        if groupName in self.groups:
            raise KeyError("Group name already exists")
        self.groups[groupName] = DeOS_PasswordGroup()

    def load(self, fname):
        """
        Load encrypted passwords from disk file, decrypt outer
        layer containing key names. Requires Trezor connected.
        @throws IOError: if reading file failed
        """
        self._load(fname)

    def _load(self, fname):
        with file(fname) as f:
            header = f.read(len(Magic.headerStr))
            if header != Magic.headerStr:
                raise IOError("Bad header in storage file")
            version = f.read(4)
            if len(version) != 4 or struct.unpack("!I", version)[0] != 1:
                raise IOError("Unknown version of storage file")
            wrappedKey = f.read(DeOS_VAULT_KEY_SIZE)
            if len(wrappedKey) != DeOS_VAULT_KEY_SIZE:
                raise IOError("Corrupted disk format - bad wrapped key length")
            self.outerKey = self.unwrapKey(wrappedKey)
            self.outerIv = f.read(DeOS_VAULT_BLOCK_SIZE)
            if len(self.outerIv) != DeOS_VAULT_BLOCK_SIZE:
                raise IOError("Corrupted disk format - bad IV length")
            lb = f.read(2)
            if len(lb) != 2:
                raise IOError("Corrupted disk format - bad backup key length")
            lb = struct.unpack("!H", lb)[0]
            self.backupKey = DeOS_Backup(self.trezor)
            serializedBackup = f.read(lb)
            if len(serializedBackup) != lb:
                raise IOError("Corrupted disk format - not enough encrypted backup key bytes")
            self.backupKey.deserialize(serializedBackup)
            ls = f.read(4)
            if len(ls) != 4:
                raise IOError("Corrupted disk format - bad data length")
            l = struct.unpack("!I", ls)[0]
            encrypted = f.read(l)
            if len(encrypted) != l:
                raise IOError("Corrupted disk format - not enough data bytes")
            hmacDigest = f.read(DeOS_VAULT_MAC_SIZE)
            if len(hmacDigest) != DeOS_VAULT_MAC_SIZE:
                raise IOError("Corrupted disk format - HMAC not complete")
            # time-invariant HMAC comparison that also works with python 2.6
            newHmacDigest = hmac.new(self.outerKey, encrypted, hashlib.sha256).digest()
            hmacCompare = 0
            for (ch1, ch2) in zip(hmacDigest, newHmacDigest):
                hmacCompare |= int(ch1 != ch2)
            if hmacCompare != 0:
                raise IOError("Corrupted disk format - HMAC does not match or bad passphrase")
            serialized = self.decryptOuter(encrypted, self.outerIv)
            self.groups = cPickle.loads(serialized)

    def save(self, fname):
        """
        Write password database to disk, encrypt it. Requires Trezor
        connected.
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
            hmacDigest = hmac.new(self.outerKey, encrypted, hashlib.sha256).digest()
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
        """
        Pad and encrypt with self.outerKey
        """
        return self._encrypt(plaintext, iv, self.outerKey)

    def _encrypt(self, plaintext, iv, key):
        """
        Pad plaintext with PKCS#5 and encrypt it.
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded = Padding(DeOS_VAULT_BLOCK_SIZE).pad(plaintext)
        return cipher.encrypt(padded)

    def decryptOuter(self, ciphertext, iv):
        """
        Decrypt with self.outerKey and unpad
        """
        return self._decrypt(ciphertext, iv, self.outerKey)

    def _decrypt(self, ciphertext, iv, key):
        """
        Decrypt ciphertext, unpad it and return
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext)
        unpadded = Padding(DeOS_VAULT_BLOCK_SIZE).unpad(plaintext)
        return unpadded

    def unwrapKey(self, wrappedOuterKey):
        """
        Decrypt wrapped outer key using Trezor.
        """
        return self._unwrap_key(wrappedOuterKey)

    def _unwrap_key(self, key):
        return self.trezor.decrypt_keyvalue(Magic.unlockNode,
                                            Magic.unlockKey,
                                            key,
                                            ask_on_encrypt=False,
                                            ask_on_decrypt=True)

    def wrapKey(self, keyToWrap):
        """
        Encrypt/wrap a key. Its size must be multiple of 16.
        """
        return self._wrap_key(keyToWrap)

    def _wrap_key(self, key):
        return self.trezor.encrypt_keyvalue(Magic.unlockNode,
                                            Magic.unlockKey,
                                            key,
                                            ask_on_encrypt=False,
                                            ask_on_decrypt=True)

    def encryptPassword(self, password, groupName):
        """
        Encrypt a password. Does PKCS#5 padding before encryption.
        Store IV as first block.

        @param groupName key that will be shown to user on Trezor and
            used to encrypt the password. A string in utf-8
        """
        return self._encrypt_password(password, groupName)

    def _encrypt_password(self, password, groupName):
        rnd = Random.new()
        rndBlock = rnd.read(DeOS_VAULT_BLOCK_SIZE)
        padded = Padding(DeOS_VAULT_BLOCK_SIZE).pad(password)
        ugroup = groupName.decode("utf-8")
        return rndBlock + self.trezor.encrypt_keyvalue(Magic.groupNode,
                                                       ugroup,
                                                       padded,
                                                       ask_on_encrypt=False,
                                                       ask_on_decrypt=True,
                                                       iv=rndBlock)

    def decryptPassword(self, encryptedPassword, groupName):
        """
        Decrypt a password. First block is IV. After decryption strips
        PKCS#5 padding.

        @param groupName key that will be shown to user on Trezor and
            was used to encrypt the password. A string in utf-8.
        """
        return self._decrypt_password(encryptedPassword, groupName)

    def _decrypt_password(self, encryptedPassword, groupName):
        ugroup = groupName.decode("utf-8")
        iv, encryptedPassword = encryptedPassword[:DeOS_VAULT_BLOCK_SIZE],\
            encryptedPassword[DeOS_VAULT_BLOCK_SIZE:]
        plain = self.trezor.decrypt_keyvalue(Magic.groupNode,
                                             ugroup,
                                             encryptedPassword,
                                             ask_on_encrypt=False,
                                             ask_on_decrypt=True,
                                             iv=iv)
        return Padding(DeOS_VAULT_BLOCK_SIZE).unpad(plain)

class DeOS_Vault(QtGui.QMainWindow):

    def __init__(self, passwds, database):
        """
        @param passwds: a PasswordMap instance w/ encrypted passwords
        @param database: file name for saving pwMap
        """
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self._set_window_title()
        self._set_modified()
        self._set_database_filename(database)
        self._set_password_map(passwds)
        self._set_selected_group()
        self._set_groups_model(header_labels=['Password group'])
        self._set_groups_filter()

    def _get_window_title(self, modified=False):
        res = self.window_title
        if modified:
            res = res+'*'*int(modified)
        return res

    def _set_selected_group(self, selected_group=None):
        self.selectedGroup = selected_group

    def _set_password_map(self, passwds):
        self.pwMap = passwds

    def _set_database_filename(self, database):
        self.dbFilename = database

    def _set_groups_filter(self):
        self.groupsFilter = QtGui.QSortFilterProxyModel()
        self.groupsFilter.setSourceModel(self.groupsModel)

    def _set_groups_model(self, header_labels):
        self.groupsModel = QtGui.QStandardItemModel()
        self.groupsModel.setHorizontalHeaderLabels(header_labels)

    def _set_modified(self, modified=False):
        self.modified = modified # modified flag "Save?" question on exit

    def _set_window_title(self, title=DeOS_VAULT_WINDOW_TITLE):
        self.window_title = title

class DeOS_VaultSettings(object):

    def __init__(self):
        self.dbFilename = None
        self.settings = QtCore.QSettings("ConstructibleUniverse", "TrezorPass")
        fname = self.settings.value("database/filename")
        if fname.isValid():
            self.dbFilename = q2s(fname.toString())

    def store(self):
        self.settings.setValue("database/filename", s2q(self.dbFilename))

class DeOS_TrezorMixin(object):
    """
    Mixin for input of passhprases.
    """

    def __init__(self, *args, **kwargs):
        super(DeOS_TrezorMixin, self).__init__(*args, **kwargs)
        self.passphrase = None

    def callback_ButtonRequest(self, msg):
        return messages_pb2.ButtonAck()

    def callback_PassphraseRequest(self, msg):
        if self.passphrase is not None:
            return messages_pb2.PassphraseAck(passphrase=self.passphrase)
        dialog = TrezorPassphraseDialog()
        if not dialog.exec_():
            sys.exit(3)
        else:
            passphrase = dialog.passphraseEdit.text()
            passphrase = unicode(passphrase)
        return messages_pb2.PassphraseAck(passphrase=passphrase)

    def callback_PinMatrixRequest(self, msg):
        dialog = EnterPinDialog()
        if not dialog.exec_():
            sys.exit(7)
        pin = q2s(dialog.pin())
        return messages_pb2.PinMatrixAck(pin=pin)

    def prefillPassphrase(self, passphrase):
        """
        Instead of asking for passphrase, use this one.
        """
        self.passphrase = passphrase.decode("utf-8")

class DeOS_TrezorClient(ProtocolMixin, DeOS_TrezorMixin, BaseClient):
    """
    Trezor client with Qt input methods
    """
    pass

class DeOS_Trezor(object):

    def __init__(self):
        self.passphrase = None

    def _get_devices(self):
        """
        Returns Trezor HID devices
        """
        return HidTransport.enumerate()
