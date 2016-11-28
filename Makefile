include .deosrc

all: build; @($(DEOS) && echo)

app:; electron ./app/

build: chmod check

check: deos.check; @(echo)

chmod:; @(chmod +x $(PRINT) $(DEOS))

clean:; -@(rm -rf node_modules/)

down:; @(vagrant destroy DeVM)

install:; @(yarn global add electron)

vm:; @(vagrant up)

yarn:; @(yarn all)
