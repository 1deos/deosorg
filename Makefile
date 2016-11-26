export MAKEFLAGS=--no-print-directory

.DEFAULT_GOAL:=all

.PHONY: all build logic ssh start vm

.SUBLIME_TARGETS: all

include .deosrc

all: deos

deos:; (chmod +x bin/deos && clear && ./bin/deos)

main:; (yarn run main)

build:; (yarn run build)

install:; (yarn install && cd app && yarn install)

dev:; (yarn run dev)

down:; (vagrant destroy DeVM)

git:; (cd ./ext/DeGIT && make all)

git.lint:; (cd ./ext/DeGIT && make lint)

git.main:; (cd ./ext/DeGIT && make main)

pug:; (yarn pug)

ssh:; (vagrant ssh -c $(VM_CMD) DeVM)

start:; (yarn start)

test:; (yarn test)

travis: logic.travis

#vm:; (vagrant up; $(MAKE) ssh)

vm:; (vagrant up)

vm.ls:; (vagrant ssh -c "cd /vagrant; bash -i -c 'ls'" DeVM)

vm.yarn.install:; (vagrant ssh -c "cd /vagrant; bash -i -c 'yarn install'" DeVM)

webpack:; (yarn all)
