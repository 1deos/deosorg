# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/trezor_chooser_dialog.ui'
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

class Ui_TrezorChooserDialog(object):
    def setupUi(self, TrezorChooserDialog):
        TrezorChooserDialog.setObjectName(_fromUtf8("TrezorChooserDialog"))
        TrezorChooserDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(TrezorChooserDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(TrezorChooserDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.trezorList = QtGui.QListWidget(TrezorChooserDialog)
        self.trezorList.setObjectName(_fromUtf8("trezorList"))
        self.verticalLayout.addWidget(self.trezorList)
        self.buttonBox = QtGui.QDialogButtonBox(TrezorChooserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TrezorChooserDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TrezorChooserDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TrezorChooserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TrezorChooserDialog)

    def retranslateUi(self, TrezorChooserDialog):
        TrezorChooserDialog.setWindowTitle(_translate("TrezorChooserDialog", "Choose Trezor to use", None))
        self.label.setText(_translate("TrezorChooserDialog", "Choose Trezor to use", None))

