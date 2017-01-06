# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/initialize_dialog.ui'
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

class Ui_InitializeDialog(object):
    def setupUi(self, InitializeDialog):
        InitializeDialog.setObjectName(_fromUtf8("InitializeDialog"))
        InitializeDialog.resize(400, 378)
        self.verticalLayout = QtGui.QVBoxLayout(InitializeDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(InitializeDialog)
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.label_3 = QtGui.QLabel(InitializeDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pwFileEdit = QtGui.QLineEdit(InitializeDialog)
        self.pwFileEdit.setObjectName(_fromUtf8("pwFileEdit"))
        self.horizontalLayout.addWidget(self.pwFileEdit)
        self.pwFileButton = QtGui.QPushButton(InitializeDialog)
        self.pwFileButton.setObjectName(_fromUtf8("pwFileButton"))
        self.horizontalLayout.addWidget(self.pwFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(InitializeDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.masterEdit1 = QtGui.QLineEdit(InitializeDialog)
        self.masterEdit1.setEchoMode(QtGui.QLineEdit.Password)
        self.masterEdit1.setObjectName(_fromUtf8("masterEdit1"))
        self.verticalLayout.addWidget(self.masterEdit1)
        self.label_2 = QtGui.QLabel(InitializeDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.masterEdit2 = QtGui.QLineEdit(InitializeDialog)
        self.masterEdit2.setEchoMode(QtGui.QLineEdit.Password)
        self.masterEdit2.setObjectName(_fromUtf8("masterEdit2"))
        self.verticalLayout.addWidget(self.masterEdit2)
        self.buttonBox = QtGui.QDialogButtonBox(InitializeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(InitializeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InitializeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InitializeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InitializeDialog)

    def retranslateUi(self, InitializeDialog):
        InitializeDialog.setWindowTitle(_translate("InitializeDialog", "Initialize master passphrase", None))
        self.textBrowser.setHtml(_translate("InitializeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is initialization step of TrezorPass. You need to choose master passphrase that will be used to unlock passwords encrypted with the device.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The passphrase is used to derive keys along with secret seed inside Trezor. If forgotten, there\'s only bruteforcing left.</p></body></html>", None))
        self.label_3.setText(_translate("InitializeDialog", "Password database file", None))
        self.pwFileButton.setText(_translate("InitializeDialog", "Select...", None))
        self.label.setText(_translate("InitializeDialog", "Master passphrase", None))
        self.label_2.setText(_translate("InitializeDialog", "Repeat master passphrase", None))

