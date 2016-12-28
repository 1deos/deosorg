import struct
import cPickle
import hmac
import hashlib

from Crypto.Cipher import AES
from Crypto import Random

from backup import Backup

from encoding import Magic, Padding

## On-disk format
#  4 bytes	header "TZPW"
#  4 bytes	data storage version, network order uint32_t
# 32 bytes	AES-CBC-encrypted wrappedOuterKey
# 16 bytes	IV
#  2 bytes	backup private key size (B)
#  B bytes	encrypted backup key
#  4 bytes	size of data following (N)
#  N bytes	AES-CBC encrypted blob containing pickled structure for password map
# 32 bytes	HMAC-SHA256 over data with same key as AES-CBC data struct above

BLOCKSIZE = 16
MACSIZE = 32
KEYSIZE = 32

class PasswordGroup(object):
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
		"""Add key-value-backud entry"""
		self.entries.append((key, encryptedValue, backupValue))
	
	def removeEntry(self, idx):
		"""Remove entry at given index"""
		self.entries.pop(idx)
	
	def updateEntry(self, idx, key, encryptedValue, backupValue):
		"""
		Update pair at index idx with given key, value and
		backup-encrypted password.
		"""
		self.entries[idx] = (key, encryptedValue, backupValue)
		
	def entry(self, idx):
		"""Return entry with given index"""
		return self.entries[idx]

class PasswordMap(object):
	"""Storage of groups of passwords in memory"""
	
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
		groupName = groupName
		if groupName in self.groups:
			raise KeyError("Password group already exists")
		
		self.groups[groupName] = PasswordGroup()

	def load(self, fname):
		"""
		Load encrypted passwords from disk file, decrypt outer
		layer containing key names. Requires Trezor connected.
		
		@throws IOError: if reading file failed
		"""
		with file(fname) as f:
			header = f.read(len(Magic.headerStr))
			if header != Magic.headerStr:
				raise IOError("Bad header in storage file")
			version = f.read(4)
			if len(version) != 4 or struct.unpack("!I", version)[0] != 1:
				raise IOError("Unknown version of storage file")
			wrappedKey = f.read(KEYSIZE)
			if len(wrappedKey) != KEYSIZE:
				raise IOError("Corrupted disk format - bad wrapped key length")
			
			self.outerKey = self.unwrapKey(wrappedKey)
			
			self.outerIv = f.read(BLOCKSIZE)
			if len(self.outerIv) != BLOCKSIZE:
				raise IOError("Corrupted disk format - bad IV length")
			
			lb = f.read(2)
			if len(lb) != 2:
				raise IOError("Corrupted disk format - bad backup key length")
			lb = struct.unpack("!H", lb)[0]
			
			self.backupKey = Backup(self.trezor)
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
			
			hmacDigest = f.read(MACSIZE)
			if len(hmacDigest) != MACSIZE:
				raise IOError("Corrupted disk format - HMAC not complete")
			
			#time-invariant HMAC comparison that also works with python 2.6
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
		assert len(self.outerKey) == KEYSIZE
		rnd = Random.new()
		self.outerIv = rnd.read(BLOCKSIZE)
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
		return self.encrypt(plaintext, iv, self.outerKey)
	
	def encrypt(self, plaintext, iv, key):
		"""
		Pad plaintext with PKCS#5 and encrypt it.
		"""
		cipher = AES.new(key, AES.MODE_CBC, iv)
		padded = Padding(BLOCKSIZE).pad(plaintext)
		return cipher.encrypt(padded)
	
	def decryptOuter(self, ciphertext, iv):
		"""
		Decrypt with self.outerKey and unpad
		"""
		return self.decrypt(ciphertext, iv, self.outerKey)
		
	def decrypt(self, ciphertext, iv, key):
		"""
		Decrypt ciphertext, unpad it and return
		"""
		cipher = AES.new(key, AES.MODE_CBC, iv)
		plaintext = cipher.decrypt(ciphertext)
		unpadded = Padding(BLOCKSIZE).unpad(plaintext)
		return unpadded
	
	def unwrapKey(self, wrappedOuterKey):
		"""
		Decrypt wrapped outer key using Trezor.
		"""
		ret = self.trezor.decrypt_keyvalue(Magic.unlockNode, Magic.unlockKey, wrappedOuterKey, ask_on_encrypt=False, ask_on_decrypt=True)
		return ret
		
	def wrapKey(self, keyToWrap):
		"""
		Encrypt/wrap a key. Its size must be multiple of 16.
		"""
		ret = self.trezor.encrypt_keyvalue(Magic.unlockNode, Magic.unlockKey, keyToWrap, ask_on_encrypt=False, ask_on_decrypt=True)
		return ret
		
	def encryptPassword(self, password, groupName):
		"""
		Encrypt a password. Does PKCS#5 padding before encryption.
		Store IV as first block.
		
		@param groupName key that will be shown to user on Trezor and
			used to encrypt the password. A string in utf-8
		"""
		rnd = Random.new()
		rndBlock = rnd.read(BLOCKSIZE)
		padded = Padding(BLOCKSIZE).pad(password)
		ugroup = groupName.decode("utf-8")
		ret = rndBlock + self.trezor.encrypt_keyvalue(Magic.groupNode, ugroup, padded, ask_on_encrypt=False, ask_on_decrypt=True, iv=rndBlock)
		return ret
		
	def decryptPassword(self, encryptedPassword, groupName):
		"""
		Decrypt a password. First block is IV. After decryption strips PKCS#5 padding.
		
		@param groupName key that will be shown to user on Trezor and
			was used to encrypt the password. A string in utf-8.
		"""
		ugroup = groupName.decode("utf-8")
		iv, encryptedPassword = encryptedPassword[:BLOCKSIZE], encryptedPassword[BLOCKSIZE:]
		plain = self.trezor.decrypt_keyvalue(Magic.groupNode, ugroup, encryptedPassword, ask_on_encrypt=False, ask_on_decrypt=True, iv=iv)
		password = Padding(BLOCKSIZE).unpad(plain)
		return password
