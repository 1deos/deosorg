# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/add_password_dialog.ui'
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

class Ui_AddPasswordDialog(object):
    def setupUi(self, AddPasswordDialog):
        AddPasswordDialog.setObjectName(_fromUtf8("AddPasswordDialog"))
        AddPasswordDialog.resize(400, 266)
        self.verticalLayout = QtGui.QVBoxLayout(AddPasswordDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AddPasswordDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.keyEdit = QtGui.QLineEdit(AddPasswordDialog)
        self.keyEdit.setMaxLength(64)
        self.keyEdit.setObjectName(_fromUtf8("keyEdit"))
        self.verticalLayout.addWidget(self.keyEdit)
        self.label_2 = QtGui.QLabel(AddPasswordDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.pwEdit1 = QtGui.QLineEdit(AddPasswordDialog)
        self.pwEdit1.setMaxLength(64)
        self.pwEdit1.setEchoMode(QtGui.QLineEdit.Password)
        self.pwEdit1.setObjectName(_fromUtf8("pwEdit1"))
        self.verticalLayout.addWidget(self.pwEdit1)
        self.label_3 = QtGui.QLabel(AddPasswordDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.pwEdit2 = QtGui.QLineEdit(AddPasswordDialog)
        self.pwEdit2.setText(_fromUtf8(""))
        self.pwEdit2.setMaxLength(64)
        self.pwEdit2.setEchoMode(QtGui.QLineEdit.Password)
        self.pwEdit2.setObjectName(_fromUtf8("pwEdit2"))
        self.verticalLayout.addWidget(self.pwEdit2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.showHideButton = QtGui.QPushButton(AddPasswordDialog)
        self.showHideButton.setObjectName(_fromUtf8("showHideButton"))
        self.horizontalLayout.addWidget(self.showHideButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(AddPasswordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddPasswordDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddPasswordDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddPasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPasswordDialog)

    def retranslateUi(self, AddPasswordDialog):
        AddPasswordDialog.setWindowTitle(_translate("AddPasswordDialog", "Add/edit password", None))
        self.label.setText(_translate("AddPasswordDialog", "Key", None))
        self.label_2.setText(_translate("AddPasswordDialog", "Password/value", None))
        self.label_3.setText(_translate("AddPasswordDialog", "Repeat password/value", None))
        self.showHideButton.setText(_translate("AddPasswordDialog", "Show/hide", None))

