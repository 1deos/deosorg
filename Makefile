include .deosrc

all:
	@ $(MAKE) install
	@ $(MAKE) run

help:
	@ echo 'export PATH="$(BIN)/darwin:$(PATH)"'

run: build
	@ $(DEOS)

build: $(OBJECTS)
	@-$(XMCC)
	@ $(CC) $(CFLAGS) -I$(INCLUDE) $(CINCLUDE) $(CTARGET) $(OBJECTS) \
		-o $(CEXE) $(CLINK)
	@ $(XMOD) $(CEXE)
	@ clear

install: clean
	@-$(MKDIR) $(BIN) $(BIN)/darwin $(EXT) $(INCLUDE) $(LIB) $(MACRO)
	@ $(MAKE) $(VIRTUAL)
	@ $(MAKE) $(SIP)
	@ $(MAKE) $(PYQT)
	@ clear

uninstall: clean
	@-$(RM) $(PYQT) $(SIP) $(VENV)
	@ clear

clean:
	@-$(RM) $(CEXE)* $(MACRO)/*.def
	@ clear

freeze:
	@ $(SETENV) && pip freeze > etc/python/requirements.txt

tdd:
	@-rm -rf app/tdd
	@-$(SETENV) && cd app && django-admin.py startproject tdd && \
		cd tdd && python manage.py migrate && python manage.py runserver &
	@-$(SETENV) && python $(TEST)/functional_tests.py
	@-rm geckodriver.log
	@-pkill -f firefox
	@-kill `ps aux | grep 'manage.py runserver' | awk '{print $2}'` \
		>/dev/null 2>/dev/null
	@-rm -rf app/tdd

test: $(TBINS)

$(BIN)/darwin/%.test: $(OBJECTS)
	@#-rm docs/atdlib/$*.dot
	@-clang -std=c89 -I$(INCLUDE) test/$*.c $(OBJECTS) -o bin/darwin/$*.test
	@-$(XMOD) bin/darwin/$*.test
	@-bin/darwin/$*.test
	@-rm $(BIN)/darwin/*.test
	@#dot -Tpng docs/atdlib/$*.dot > var/img/$*.png

vault: $(UI_GENERATED)
	@-rm $(VAULT)/src/*.pyc
	@-rm -rf $(VAULT)/src/atdlib
	@-mkdir $(VAULT)/src/atdlib
	@-touch $(VAULT)/src/atdlib/__init__.py
	@-cp $(SRC)/vault.py $(VAULT)/src/atdlib/vault.py
	@-$(SETENV) && python $(VAULT)/src/vault.py
	@-rm $(VAULT)/src/*.pyc
	@-rm -rf $(VAULT)/src/atdlib

vault.sdk:
	@-$(SETENV) && python src/vault.py

$(VAULT)/src/ui_%.py: $(VAULT)/view/%.ui
	@-$(SETENV) && $(VENV)/bin/pyuic4 -o $@ $<

$(OBJ)/%.o: $(LIB)/%.c $(INCLUDE)/%.h
	@-rm $(OBJ)/$*.o
	@ $(CC) -std=c89 -Wall -g -I$(INCLUDE) -c $(LIB)/$*.c -o $(OBJ)/$*.o
	@ clear

$(VIRTUAL):
	@-$(MKDIR) venv $(VIRTUAL)
	@ $(NEWENV) $(VENV)
	@ $(SETENV) && $(PIP) install -r $(REQUIRE)
	@ clear

$(PYQT):
	@ cp $(EXT)/.cache/PyQt-mac-gpl-4.11.4.tar.gz $(EXT)/pyqt.tar.gz
	@ gunzip $(EXT)/pyqt.tar.gz && tar -xvf $(EXT)/pyqt.tar
	@-$(RM) $(EXT)/pyqt.tar
	@ mv PyQt-mac-gpl-4.11.4 $(EXT)/pyqt
	@ $(SETENV) && cd $(EXT)/pyqt && \
	  python configure-ng.py --confirm-license --qmake=$(QMAKE) && \
	  make && make install
	@ clear

$(SIP):
	@ cp $(EXT)/.cache/sip-4.18.1.tar.gz $(EXT)/sip.tar.gz
	@ gunzip $(EXT)/sip.tar.gz && tar -xvf $(EXT)/sip.tar
	@-$(RM) $(EXT)/sip.tar
	@ mv sip-4.18.1 $(EXT)/sip
	@ $(SETENV) && cd $(EXT)/sip && \
	  python configure.py --incdir=$(VENV)/include/python2.7 && \
	  make && make install
	@ clear
