# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/trezor_passphrase_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TrezorPassphraseDialog(object):
    def setupUi(self, TrezorPassphraseDialog):
        TrezorPassphraseDialog.setObjectName(_fromUtf8("TrezorPassphraseDialog"))
        TrezorPassphraseDialog.resize(400, 133)
        self.verticalLayout = QtGui.QVBoxLayout(TrezorPassphraseDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(TrezorPassphraseDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.passphraseEdit = QtGui.QLineEdit(TrezorPassphraseDialog)
        self.passphraseEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passphraseEdit.setObjectName(_fromUtf8("passphraseEdit"))
        self.verticalLayout.addWidget(self.passphraseEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(TrezorPassphraseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TrezorPassphraseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TrezorPassphraseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TrezorPassphraseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TrezorPassphraseDialog)

    def retranslateUi(self, TrezorPassphraseDialog):
        TrezorPassphraseDialog.setWindowTitle(_translate("TrezorPassphraseDialog", "Dialog", None))
        self.label.setText(_translate("TrezorPassphraseDialog", "Enter passphrase for Trezor:", None))

