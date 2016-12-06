ext.bitcoin: bitcoin.all

bitcoin.all: bitcoin.install
	@$(PRINT) purple $@ start
	-rm -rf $(BASEDIR)/.tmp
	@$(PRINT) purple $@ stop

bitcoin.install: bitcoin.clone
	@$(PRINT) purple $@ start
	mv $(BASEDIR)/.tmp/bitcoin/doc $(BASEDIR)/var/docs/bitcoin
	mv $(BASEDIR)/.tmp/bitcoin/README.md $(BASEDIR)/var/docs/bitcoin/README.md
	mv $(BASEDIR)/.tmp/bitcoin/lib/crypto/*.c $(BASEDIR)/src/crypto/
	mv $(BASEDIR)/.tmp/bitcoin/include/ccoin/crypto/*.h $(BASEDIR)/src/crypto/
	rm -rf $(BASEDIR)/.tmp/bitcoin/include/ccoin/crypto/
	rm -rf $(BASEDIR)/.tmp/bitcoin/lib/crypto/
	mv $(BASEDIR)/.tmp/bitcoin/lib/net $(BASEDIR)/src/net/lib
	mv $(BASEDIR)/.tmp/bitcoin/lib $(BASEDIR)/src/bitcoin/lib
	mv $(BASEDIR)/.tmp/bitcoin/src/*.c $(BASEDIR)/src/bitcoin/
	mv $(BASEDIR)/.tmp/bitcoin/src/*.h $(BASEDIR)/src/bitcoin/
	mv $(BASEDIR)/.tmp/bitcoin/include/ccoin/net $(BASEDIR)/src/net/include
	mv $(BASEDIR)/.tmp/bitcoin/include/ccoin $(BASEDIR)/src/bitcoin/include
	mv $(BASEDIR)/.tmp/bitcoin/test $(BASEDIR)/src/test/bitcoin
	@$(PRINT) purple $@ stop

bitcoin.clone: bitcoin.clean
	@$(PRINT) purple $@ start
	cd $(BASEDIR)/.tmp && git clone $(GIT_BITCOIN)
	@$(PRINT) purple $@ stop

bitcoin.clean:
	@$(PRINT) purple $@ start
	-rm -rf $(BASEDIR)/.tmp
	-mkdir $(BASEDIR)/.tmp
	-rm -rf $(BASEDIR)/var/docs/bitcoin
	-rm -rf $(BASEDIR)/src/bitcoin
	-mkdir $(BASEDIR)/src/bitcoin
	-rm -rf $(BASEDIR)/src/crypto
	-mkdir $(BASEDIR)/src/crypto
	-rm -rf $(BASEDIR)/src/net
	-mkdir $(BASEDIR)/src/net
	-rm -rf $(BASEDIR)/src/test/bitcoin
	@$(PRINT) purple $@ stop
