export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all
.PHONY: all build dev test
.SUBLIME_TARGETS: all

include .deosrc

all: build
	@$(PRINT) purple $@ start
	$(PATH_BIN)/deos
	@$(PRINT) purple $@ stop

test:
	nvm --version

build:
	@chmod +x $(PRINT)
	@$(PRINT) yellow $@ start
	$(CC) -std=c89 -Wall -g -pthread $(PATH_DOJO)/main.c -o $(PATH_BIN)/deos
	chmod +x $(PATH_BIN)/deos
	@$(PRINT) yellow $@ stop

dev: down
	vagrant up
	vagrant ssh -c "cd /vagrant; bash -i -c 'ipython --profile=vagrant'"

down:
	vagrant destroy
