export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL := all
.PHONY: all build clean install save watch
.SUBLIME_TARGETS: all

include .deosrc

all: yarn

# SWAP BEGIN
all.swap: build.swap
	yarn run all
# SWAP END

dev:
	@$(PRINT) yellow $@ start
	yarn run dev
	@$(PRINT) yellow $@ stop

lint: clean node_modules
	@$(PRINT) yellow $@ start
	yarn run lint
	@$(PRINT) yellow $@ stop

# SWAP BEGIN
build.swap: clean.swap node_modules
	open dojo/index.html
# SWAP END

# SWAP BEGIN
clean.swap: save.swap
	yarn run clean
	-ps aux | awk '/node/{print $2}' | xargs kill -9
	-rm -rf ./node_modules/
	$(MAKE) save
# SWAP END

node_modules:
	yarn install

# SWAP BEGIN
save.swap:
	-git add .
	-git commit -S -m "checkpoint"
# SWAP END

# SWAP BEGIN
watch.swap:
	yarn run watch
# SWAP END

clean:
	@chmod +x $(PRINT) && clear
	@$(PRINT) yellow $@ start
ifeq ($(DEOS_CLEAN_ALL),$(IS_TRUE))
	-rm -rf ./node_modules/
	-rm -rf ./app/node_modules/
endif
	-rm $(CLEAN_APP)
	-rm -rf $(CLEAN_BUILD)
	@$(PRINT) yellow $@ stop
