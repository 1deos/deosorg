from PyQt4 import QtGui, QtCore

from ui_addgroup_dialog import Ui_AddGroupDialog
from ui_trezor_passphrase_dialog import Ui_TrezorPassphraseDialog
from ui_add_password_dialog import Ui_AddPasswordDialog
from ui_initialize_dialog import Ui_InitializeDialog
from ui_enter_pin_dialog import Ui_EnterPinDialog
from ui_trezor_chooser_dialog import Ui_TrezorChooserDialog

class AddGroupDialog(QtGui.QDialog, Ui_AddGroupDialog):
	
	def __init__(self, groups):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.newGroupEdit.textChanged.connect(self.validate)
		self.groups = groups
		
		#disabled for empty string
		button = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
		button.setEnabled(False)
	
	def newGroupName(self):
		return self.newGroupEdit.text()
		
	
	def validate(self):
		"""
		Validates input if name is not empty and is different from
		existing group names.
		"""
		valid = True
		text = self.newGroupEdit.text()
		if text.isEmpty():
			valid = False
		
		if unicode(text).encode("utf-8") in self.groups:
			valid = False
		
		button = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
		button.setEnabled(valid)
	
class TrezorPassphraseDialog(QtGui.QDialog, Ui_TrezorPassphraseDialog):
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
	
	def passphrase(self):
		return self.passphraseEdit.text()
		
	

class AddPasswordDialog(QtGui.QDialog, Ui_AddPasswordDialog):
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.pwEdit1.textChanged.connect(self.validatePw)
		self.pwEdit2.textChanged.connect(self.validatePw)
		self.showHideButton.clicked.connect(self.switchPwVisible)
	
	def key(self):
		return self.keyEdit.text()
	
	def pw1(self):
		return self.pwEdit1.text()
	
	def pw2(self):
		return self.pwEdit2.text()
	
	def validatePw(self):
		same = self.pw1() == self.pw2()
		button = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
		button.setEnabled(same)
	
	def switchPwVisible(self):
		pwMode = self.pwEdit1.echoMode()
		if pwMode == QtGui.QLineEdit.Password:
			newMode = QtGui.QLineEdit.Normal
		else:
			newMode = QtGui.QLineEdit.Password
			
		self.pwEdit1.setEchoMode(newMode)
		self.pwEdit2.setEchoMode(newMode)
		
class InitializeDialog(QtGui.QDialog, Ui_InitializeDialog):
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.masterEdit1.textChanged.connect(self.validate)
		self.masterEdit2.textChanged.connect(self.validate)
		self.pwFileEdit.textChanged.connect(self.validate)
		self.pwFileButton.clicked.connect(self.selectPwFile)
		self.validate()
	
	def pw1(self):
		return self.masterEdit1.text()
	
	def pw2(self):
		return self.masterEdit2.text()
	
	def pwFile(self):
		return self.pwFileEdit.text()
	
	def validate(self):
		"""
		Enable OK button only if both master and backup are repeated
		without typo and some password file is selected.
		"""
		same = self.pw1() == self.pw2()
		fileSelected = not self.pwFileEdit.text().isEmpty()
		button = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
		button.setEnabled(same and fileSelected)
	
	def selectPwFile(self):
		"""
		Show file dialog and return file user chose to store the
		encrypted password database.
		"""
		path = QtCore.QDir.currentPath()
		dialog = QtGui.QFileDialog(self, "Select password database file",
			path, "(*.pwdb)")
		dialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
		
		res = dialog.exec_()
		if not res:
			return
		
		fname = dialog.selectedFiles()[0]
		self.pwFileEdit.setText(fname)

class EnterPinDialog(QtGui.QDialog, Ui_EnterPinDialog):
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.pb1.clicked.connect(self.pinpadPressed)
		self.pb2.clicked.connect(self.pinpadPressed)
		self.pb3.clicked.connect(self.pinpadPressed)
		self.pb4.clicked.connect(self.pinpadPressed)
		self.pb5.clicked.connect(self.pinpadPressed)
		self.pb6.clicked.connect(self.pinpadPressed)
		self.pb7.clicked.connect(self.pinpadPressed)
		self.pb8.clicked.connect(self.pinpadPressed)
		self.pb9.clicked.connect(self.pinpadPressed)
	
	def pin(self):
		return self.pinEdit.text()
	
	def pinpadPressed(self):
		sender = self.sender()
		objName = sender.objectName()
		digit = objName[-1]
		self.pinEdit.setText(self.pinEdit.text() + digit)
	
class TrezorChooserDialog(QtGui.QDialog, Ui_TrezorChooserDialog):
	
	def __init__(self, deviceMap):
		"""
		Create dialog and fill it with labels from deviceMap
		
		@param deviceMap: dict device string -> device label
		"""
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		for deviceStr, label in deviceMap.items():
			item = QtGui.QListWidgetItem(label)
			item.setData(QtCore.Qt.UserRole, QtCore.QVariant(deviceStr))
			self.trezorList.addItem(item)
		self.trezorList.setCurrentRow(0)
	
	def chosenDeviceStr(self):
		"""
		Returns device string of chosen Trezor
		"""
		itemData = self.trezorList.currentItem().data(QtCore.Qt.UserRole)
		deviceStr = str(itemData.toString())
		return deviceStr
	
