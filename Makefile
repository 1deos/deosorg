export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all

.PHONY:all build chmod clean install main picocoin run venv

.SUBLIME_TARGETS:all

include .deosrc

all: run
	@$(PRINT) yellow $@ start
ifeq ($(HOST_OS), $(IS_MAC))
	(vagrant ssh -c $(SSHCMD) DeVM)
else
	@(echo "'make $@' isn't yet supported on $(HOST_OS).")
endif
	@$(PRINT) yellow $@ stop

run: venv
	@$(PRINT) yellow $@ start
ifeq ($(HOST_OS), $(IS_MAC))
	(python $(SRC)/main.py)
else
	@(echo "'make $@' isn't yet supported on $(HOST_OS).")
endif
	@$(PRINT) yellow $@ stop

venv:
	@$(PRINT) yellow $@ start
ifeq ($(HOST_OS), $(IS_MAC))
	@-(rm -rf $(VENV)/darwin/python/)
	(cd $(VENV)/darwin/ && virtualenv python --no-site-packages)
	(cp $(SRC)/templates/dotfiles/gitignore.txt \
		$(VENV)/darwin/python/.gitignore)
else
	@(echo "'make $@' isn't yet supported on $(HOST_OS).")
endif
	@$(PRINT) yellow $@ stop

main:
	@$(PRINT) yellow $@ start
	@-(rm -rf $(BIN)/main*)
	($(CC) -std=c89 -Wall -g -pthread -I$(LIB) $(SRC)/main.c -o $(BIN)/main)
	(chmod +x $(BIN)/main)
	($(BIN)/main)
	@$(PRINT) yellow $@ stop

app:; electron ./app/

build: chmod check

check: deos.check; @(echo)

chmod:; (chmod +x $(PRINT) $(DEOS))

ext: ext.bitcoin ext.two1

install:; (yarn global add electron)

js:; (yarn run gulp && yarn run test)

rm: vm.uninstall

sh: vm.ssh

vm: vm.install

zt: zt.install
