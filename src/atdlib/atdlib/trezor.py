#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import sys

from trezorlib.client import BaseClient, ProtocolMixin
from trezorlib.transport_hid import HidTransport
from trezorlib import messages_pb2

__all__ = ["Trezor", "TrezorMixin", "TrezorClient"]

class Trezor(object):

    def __init__(self):
        """ Trezor Bitcoin Hardware Wallet
        """
        self.passphrase = None

    def _get_devices(self):
        """ Trezor HID Devices
        """
        return HidTransport.enumerate()

class TrezorMixin(object):

    def __init__(self, *args, **kwargs):
        """ Mixin for Input of Passhprases
        """
        super(TrezorMixin, self).__init__(*args, **kwargs)
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
        """ Instead of asking for passphrase, use this one.
        """
        self.passphrase = passphrase.decode("utf-8")

class TrezorClient(ProtocolMixin, TrezorMixin, BaseClient):
    """ Trezor Client w/ Qt Input Methods
    """
    pass
