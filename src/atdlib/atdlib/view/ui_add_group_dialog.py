# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/vault/template/addgroup_dialog.ui'
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

class Ui_AddGroupDialog(object):
    def setupUi(self, AddGroupDialog):
        AddGroupDialog.setObjectName(_fromUtf8("AddGroupDialog"))
        AddGroupDialog.resize(415, 111)
        self.verticalLayout = QtGui.QVBoxLayout(AddGroupDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AddGroupDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.newGroupEdit = QtGui.QLineEdit(AddGroupDialog)
        self.newGroupEdit.setMaxLength(64)
        self.newGroupEdit.setObjectName(_fromUtf8("newGroupEdit"))
        self.verticalLayout.addWidget(self.newGroupEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(AddGroupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddGroupDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddGroupDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddGroupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddGroupDialog)

    def retranslateUi(self, AddGroupDialog):
        AddGroupDialog.setWindowTitle(_translate("AddGroupDialog", "Add new group", None))
        self.label.setText(_translate("AddGroupDialog", "Name of new group", None))

