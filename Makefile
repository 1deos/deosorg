export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all

.PHONY:all bin bitcoin build check chmod clean init rm sh venv vm

.SUBLIME_TARGETS:all

include .deosrc

all: chmod
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@(if [[ -z "$(x)" ]];    then ($(MAKE) install); fi)
	@(if [[ -n "$(x)" ]];    then ($(PRINTM) cyan $@ start); fi)
	if   [ "$(x)" = "all" ]; then ($(MAKE) build)\
	else [ "$(x)" = "run" ]    && ($(MAKE) wallet) || ($(MAKE) x=all); fi
	@(if [[ -n "$(x)" ]];    then ($(PRINTM) cyan $@ stop); fi)
endif

install:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	sh $(BASEDIR)/src/install.sh
endif

chmod:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@-chmod +x $(PRINTM) $(DEOS)
endif

build: venv check
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) cyan $@ start
	-mkdir $(BASEDIR)/config/nginx/
	-$(MAKE) vm
	@$(PRINTM) cyan $@ stop
endif

clean:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) magenta $@ start
	@-$(MAKE) rm
	@-rm -rf $(BASEDIR)/.blockstack/
	@-rm -rf $(BASEDIR)/.vagrant/
	@-rm -rf $(BASEDIR)/.zerotier/
	@$(PRINTM) magenta $@ stop
endif

check:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) cyan $@ start
	@-$(MAKE) deos.check
	@$(PRINTM) cyan $@ stop
else
	@-$(MAKE) deos.check
endif

venv:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) cyan $@ start
	[ "$(x)" = "blockstack" ]\
	&& (cd $(VENV)/darwin/\
		&& virtualenv blockstack --no-site-packages)\
	|| (cd $(VENV)/darwin/\
		&& virtualenv default --no-site-packages)
	@$(PRINTM) cyan $@ stop
endif

rm:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) yellow $@ start
	-rm -rf $(BASEDIR)/.deos/
	#[ -d $(BASEDIR)/.vagrant/ ] && rm -rf $(BASEDIR)/.deos/
	-$(MAKE) vm.uninstall
	@$(PRINTM) yellow $@ stop
endif

sh:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) cyan $@ start
	-$(MAKE) vm.ssh
	@$(PRINTM) cyan $@ stop
endif

vm:
ifeq ($(DeOS_HOST_OS),$(IS_MAC))
	@$(PRINTM) cyan $@ start
	-$(MAKE) vm.install
	@$(PRINTM) cyan $@ stop
endif

yubikey:
	@$(PRINTM) cyan $@ start
	$(DeOS_YUBIKEY_PATH_SRC)/yubiserve.py --db $(DeOS_YUBIKEY_PATH_DB)
	@$(PRINTM) cyan $@ stop

wallet:
	@-$(PRINTM) cyan $@ start
	#brew install libusb-1.0-0
	# clean
	-rm -rf $(VENV)/darwin/wallet/
	# init
	cd $(VENV)/darwin/ && virtualenv wallet --no-site-packages
	# install
	source .deos/venv/darwin/wallet/bin/activate\
	&& pip install pyusb --pre\
	&& pip install pypreprocessor
	# build
	source .deos/venv/darwin/wallet/bin/activate\
	&& cd src\
	&& python wallet.py prod
	# run
	source .deos/venv/darwin/wallet/bin/activate\
	&& chmod +x bin/wallet\
	&& ./bin/wallet
	@-$(PRINTM) cyan $@ stop
