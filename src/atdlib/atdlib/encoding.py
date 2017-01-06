#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import struct

from PyQt4 import QtCore

__all__ = ["q2s", "s2q", "Magic", "Padding"]

def q2s(s):
    """ QString -> UTF-8 string object
    """
    return str(s.toUtf8())

def s2q(s):
    """ UTF-8 encoded string -> QString
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
    """ PKCS#7 Padding for block cipher having 16-byte blocks
    """

    def __init__(self, blocksize):
        self.blocksize = blocksize

    def pad(self, s):
        BS = self.blocksize
        return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    def unpad(self, s):
        return s[0:-ord(s[-1])]
