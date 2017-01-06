# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/enter_pin_dialog.ui'
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

class Ui_EnterPinDialog(object):
    def setupUi(self, EnterPinDialog):
        EnterPinDialog.setObjectName(_fromUtf8("EnterPinDialog"))
        EnterPinDialog.resize(359, 300)
        self.verticalLayout = QtGui.QVBoxLayout(EnterPinDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(EnterPinDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pb7 = QtGui.QPushButton(EnterPinDialog)
        self.pb7.setObjectName(_fromUtf8("pb7"))
        self.gridLayout.addWidget(self.pb7, 1, 0, 1, 1)
        self.pb8 = QtGui.QPushButton(EnterPinDialog)
        self.pb8.setObjectName(_fromUtf8("pb8"))
        self.gridLayout.addWidget(self.pb8, 1, 1, 1, 1)
        self.pb9 = QtGui.QPushButton(EnterPinDialog)
        self.pb9.setObjectName(_fromUtf8("pb9"))
        self.gridLayout.addWidget(self.pb9, 1, 2, 1, 1)
        self.pinEdit = QtGui.QLineEdit(EnterPinDialog)
        self.pinEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pinEdit.setObjectName(_fromUtf8("pinEdit"))
        self.gridLayout.addWidget(self.pinEdit, 4, 0, 1, 3)
        self.pb4 = QtGui.QPushButton(EnterPinDialog)
        self.pb4.setObjectName(_fromUtf8("pb4"))
        self.gridLayout.addWidget(self.pb4, 2, 0, 1, 1)
        self.pb5 = QtGui.QPushButton(EnterPinDialog)
        self.pb5.setObjectName(_fromUtf8("pb5"))
        self.gridLayout.addWidget(self.pb5, 2, 1, 1, 1)
        self.pb6 = QtGui.QPushButton(EnterPinDialog)
        self.pb6.setObjectName(_fromUtf8("pb6"))
        self.gridLayout.addWidget(self.pb6, 2, 2, 1, 1)
        self.pb1 = QtGui.QPushButton(EnterPinDialog)
        self.pb1.setObjectName(_fromUtf8("pb1"))
        self.gridLayout.addWidget(self.pb1, 3, 0, 1, 1)
        self.pb2 = QtGui.QPushButton(EnterPinDialog)
        self.pb2.setObjectName(_fromUtf8("pb2"))
        self.gridLayout.addWidget(self.pb2, 3, 1, 1, 1)
        self.pb3 = QtGui.QPushButton(EnterPinDialog)
        self.pb3.setObjectName(_fromUtf8("pb3"))
        self.gridLayout.addWidget(self.pb3, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(EnterPinDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EnterPinDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EnterPinDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EnterPinDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EnterPinDialog)
        EnterPinDialog.setTabOrder(self.pinEdit, self.pb8)
        EnterPinDialog.setTabOrder(self.pb8, self.pb9)
        EnterPinDialog.setTabOrder(self.pb9, self.buttonBox)
        EnterPinDialog.setTabOrder(self.buttonBox, self.pb7)
        EnterPinDialog.setTabOrder(self.pb7, self.pb4)
        EnterPinDialog.setTabOrder(self.pb4, self.pb5)
        EnterPinDialog.setTabOrder(self.pb5, self.pb6)
        EnterPinDialog.setTabOrder(self.pb6, self.pb1)
        EnterPinDialog.setTabOrder(self.pb1, self.pb2)
        EnterPinDialog.setTabOrder(self.pb2, self.pb3)

    def retranslateUi(self, EnterPinDialog):
        EnterPinDialog.setWindowTitle(_translate("EnterPinDialog", "Enter PIN", None))
        self.label.setText(_translate("EnterPinDialog", "Enter PIN", None))
        self.pb7.setText(_translate("EnterPinDialog", "?", None))
        self.pb8.setText(_translate("EnterPinDialog", "?", None))
        self.pb9.setText(_translate("EnterPinDialog", "?", None))
        self.pb4.setText(_translate("EnterPinDialog", "?", None))
        self.pb5.setText(_translate("EnterPinDialog", "?", None))
        self.pb6.setText(_translate("EnterPinDialog", "?", None))
        self.pb1.setText(_translate("EnterPinDialog", "?", None))
        self.pb2.setText(_translate("EnterPinDialog", "?", None))
        self.pb3.setText(_translate("EnterPinDialog", "?", None))

