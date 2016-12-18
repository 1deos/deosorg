yubikey.build: yubikey.clone
	$(DeOS_YUBIKEY_PATH_TOOLS)/dbcreate.py $(DeOS_YUBIKEY_PATH_DB)
	$(DeOS_YUBIKEY_PATH_TOOLS)/flash.py $(DeOS_YUBIKEY_USER)\
	                                    $(DeOS_YUBIKEY_PATH_DB)
	$(DeOS_YUBIKEY_PATH_TOOLS)/dbconf.py -aa $(DeOS_YUBIKEY_APP)\
	                                         $(DeOS_YUBIKEY_PATH_DB)

yubikey.clone: yubikey.clean
	-git rm --cached dev/yubikey
	-git submodule add --force $(DeOS_YUBIKEY_GIT_REPO) dev/yubikey

yubikey.clean:
	-rm .gitmodules #FIXME
	-rm -rf dev/yubikey

yubikey.install:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	brew install ykpers
endif
