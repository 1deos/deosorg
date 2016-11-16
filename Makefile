export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all

.PHONY: all build

.SUBLIME_TARGETS: all

include .deosrc

all: build
	@$(PRINT) purple $@ start
	$(PATH_BIN)/deos
	@$(PRINT) purple $@ stop

build:
	@chmod +x $(PRINT)
	@$(PRINT) yellow $@ start
	$(CC) -std=c89 -Wall -g -pthread $(PATH_DOJO)/main.c -o $(PATH_BIN)/deos
	chmod +x $(PATH_BIN)/deos
	@$(PRINT) yellow $@ stop
