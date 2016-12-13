zt.install:
	@$(PRINT) yellow $@ start
	cd $(BASEDIR)/ext/zerotier && sudo make install
	@$(PRINT) yellow $@ stop
