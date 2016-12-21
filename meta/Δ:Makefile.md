# `Makefile`

## Schema

```yaml
type: object

required:
- makeflags
- default_goal
- phony
- sublime_targets
- config_file
- all
- two

properties:
  makeflags: {type: string}
  default_goal: {type: string}
  phony: {type: string}
  sublime_targets: {type: string}
  config_file: {type: string}

  all:
    type: object
    required: [hook, 'if:host;is:mac', else]
    hook:
      type: object
      required: [pre, post]

  two:
    type: object
    required: [hook, 'if:host;is:mac', else]
    hook:
      type: object
      required: [pre, post]
```

## Environment

```yaml
makeflags: --no-print-directory
default_goal: all
phony: all meta
sublime_targets: all
config_file: .deosrc

all:
  hook:
    pre: >
      @echo && $(PRINT) cyan $@ start
    post: >
      @$(PRINT) cyan $@ stop && echo
  if:host;is:mac: >
    @(python src/hello.py)
  else: >
    @(echo "'make $@' isn't yet supported on $(DeOS_HOST_OS).")

two:
  hook:
    pre: >
      @echo && $(PRINT) cyan $@ start
    post: >
      @$(PRINT) cyan $@ stop && echo
  if:host;is:mac: >
    @(python src/hello.py)
  else: >
    @(echo "'make $@' isn't yet supported on $(DeOS_HOST_OS).")
```

## Template

```makefile
Δ with (data=None)

export MAKEFLAGS=Δ(data['makeflags'])

.DEFAULT_GOAL:=Δ(data['default_goal'])
.PHONY:Δ(data['phony'])
.SUBLIME_TARGETS:Δ(data['sublime_targets'])

DeOS_ADD_DOTDEOS:=mkdir .deos .deos/bin .deos/bin/darwin .deos/bin/vagrant .deos/bin/travis .deos/obj .deos/obj/darwin .deos/obj/vagrant .deos/obj/travis .deos/venv .deos/venv/darwin .deos/venv/vagrant .deos/venv/travis
DeOS_ADD_TRAVIS:=gem install travis --no-rdoc --no-ri
DeOS_BIN_TRAVIS:=$(shell which travis)
DeOS_RM_DOTDEOS:=rm -rf .deos

all: #clean install build venv lint
#    Δ(data['all']['hook']['pre'])
#ifeq ($(DeOS_HOST_OS),$(IS_MAC))
    Δ(data['all']['if:host;is:mac'])
#else
#    Δ(data['all']['else'])
#endif
#    Δ(data['all']['hook']['post'])

wiki: wiki.clone

wiki.clone:
    -rm -rf var/wiki/
    cd var/ && git clone git@github.com:DeSantisInc/DeOS.wiki.git wiki
    rm -rf var/wiki/.git/

webpy: webpy.clone

webpy.clone:
    -rm -rf src/web/
    cd src/ && git clone git@github.com:webpy/webpy.git web
    rm -rf src/web/.git/
    rm src/web/.gitignore
    rm src/web/.travis.yml
    mv src/web/test/ test/web/
    mv src/web/docs/ doc/web/
    mv src/web/README.md doc/web/README.md
    mv src/web/LICENSE.txt doc/web/LICENSE.txt
    mv src/web/ChangeLog.txt doc/web/ChangeLog.txt

two: #clean install build venv lint
#    Δ(data['two']['hook']['pre'])
#ifeq ($(DeOS_HOST_OS),$(IS_MAC))
    Δ(data['two']['if:host;is:mac'])
#else
#    Δ(data['two']['else'])
#endif
#    Δ(data['two']['hook']['post'])

meta:
    sh bootstrap.sh
    python src/hello.py
    $(MAKE) wiki
    $(MAKE) webpy

clean:
    @([ -d ".deos" ] && $(DeOS_RM_DOTDEOS) || echo "$@:else")

install:
    @([ ! -x "$(DeOS_BIN_TRAVIS)" ] && $(DeOS_ADD_TRAVIS) || echo "$@:else")

build:
    @([ ! -d ".deos" ] && $(DeOS_ADD_DOTDEOS) || echo "$@:else")

venv:
    @([ -d ".deos/venv" ] && rm -rf .deos/venv || echo "$@:else")
    @([ ! -d ".deos/venv" ] && mkdir .deos/venv .deos/venv/darwin .deos/venv/vagrant .deos/venv/travis || echo "$@:else")

lint:
    @(travis lint .travis.yml)
```
