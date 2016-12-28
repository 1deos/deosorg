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
- bips
- build
- cache
- clean
- install
- lint
- meta
- terminal
- venv
- vm
- webpy
- wiki
- wikiup

properties:
  makeflags: {type: string}
  default_goal: {type: string}
  phony: {type: string}
  sublime_targets: {type: string}
  config_file: {type: string}

  all:
    type: object
    required: [hook, if, else]

  vm:
    type: object
    required: [hook, if, else]

  bips:
    type: object
    required: [hook, if, else]

  build:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  cache:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  clean:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  install:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  lint:
    type: object
    required: [hook, 'if:host;is:mac', 'else:host']
    hook:
      type: object
      required: [pre, post]

  meta:
    type: object
    required: [hook, 'else:host']
    properties:
      else:host: {type: string}
      hook:
        type: object
        required: [logger, printm]
        properties:
          logger:
            type: object
            required: [pre, post]
            properties:
              pre: {type: string}
              post: {type: string}
          printm:
            type: object
            required: [pre, post]
            properties:
              pre: {type: string}
              post: {type: string}

  terminal:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  venv:
    type: object
    required: [hook, 'else:host']
    hook:
      type: object
      required: [pre, post]

  webpy:
    type: object
    required: [hook, 'if:repo;is:cached', 'else:repo', 'else:host']
    hook:
      type: object
      required: [pre, post]

  wiki:
    type: object
    required: [hook, if, else]

  wikiup:
    type: object
    required: [hook, 'else:host']
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
    pre:
      do:
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")'
      - '@ ($(PRINTM) cyan $@ start)'
    post:
      do:
      - '@ ($(PRINTM) cyan $@ stop)'
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")'
  if:
    host:
      is:
        mac:
          do:
          - '@ (python src/hello.py)'
  else:
    host:
      do:
      - "@ (echo \"'make $@' isn't yet supported on $(HOSTOS).\")"

vm:
  hook:
    pre:
      do:
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")'
      - '@ ($(PRINTM) cyan $@ start)'
    post:
      do:
      - '@ ($(PRINTM) cyan $@ stop)'
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")'
  if:
    host:
      is:
        mac:
          do:
          - '@-([   -d "$(BASEDIR)/.vagrant/" ] && vagrant destroy DeVM --force)'
          - '@-([   -d "$(BASEDIR)/.vagrant/" ] && rm -rf $(BASEDIR)/.vagrant/)'
          - '@ ([ ! -d "$(BASEDIR)/.vagrant/" ] && $(SPINNER) $(UPCMD))'
  else:
    host:
      do:
      - "@ (echo \"'make $@' isn't yet supported on $(HOSTOS).\")"

bips:
  hook:
    pre:
      do:
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")'
      - '@ ($(PRINTM) magenta $@ start)'
    post:
      do:
      - '@ ($(PRINTM) magenta $@ stop)'
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")'
  if:
    host:
      is:
        mac:
          do:
          - '@-(rm -rf docs/bips)'
          - '@ (cd docs && git clone $(DeOS_GIT_REPO_BIPS))'
          - '@ (rm -rf docs/bips/.git)'
  else:
    host:
      do:
      - "@ (echo \"'make $@' isn't yet supported on $(HOSTOS).\")"

build:
  hook:
    pre: $(PRINTM) yellow $@ start
    post: $(PRINTM) yellow $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

cache:
  hook:
    pre: $(PRINTM) magenta $@ start
    post: $(PRINTM) magenta $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

clean:
  hook:
    pre: $(PRINTM) cyan $@ start
    post: $(PRINTM) cyan $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

install:
  hook:
    pre: $(PRINTM) yellow $@ start
    post: $(PRINTM) yellow $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

lint:
  hook:
    pre: $(PRINTM) magenta $@ start
    post: $(PRINTM) magenta $@ stop
  if:host;is:mac: travis lint .travis.yml
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

meta:
  make:
  - cache
  - wiki
  - webpy
  - terminal
  - bips
  - pycpp
  hook:
    logger:
      pre: '$(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0"'
      post: '$(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1"'
    printm:
      pre: $(PRINTM) yellow $@ start
      post: $(PRINTM) yellow $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

terminal:
  hook:
    pre: $(PRINTM) cyan $@ start
    post: $(PRINTM) cyan $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

venv:
  hook:
    pre: $(PRINTM) yellow $@ start
    post: $(PRINTM) yellow $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

webpy:
  hook:
    pre: $(PRINTM) magenta $@ start
    post: $(PRINTM) magenta $@ stop
  if:repo;is:cached: (cp .cache/webpy.tar.gz src/web.tar.gz && gunzip src/web.tar.gz && cd src && tar -xvf web.tar && mv webpy web)
  else:repo: cd src && git clone $(DeOS_GIT_REPO_WEB) web
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

wiki:
  hook:
    pre:
      do:
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")'
      - '@ ($(PRINTM) cyan $@ start)'
    post:
      do:
      - '@ ($(PRINTM) cyan $@ stop)'
      - '@ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")'
  if:
    host:
      is:
        mac:
          do:
          - '@-(rm -rf var/wiki)'
          - '@ (cd var && git clone $(DeOS_GIT_REPO_WIKI) wiki)'
          - '@ (rm -rf var/wiki/.git)'
  else:
    host:
      do:
      - "@ (echo \"'make $@' isn't yet supported on $(HOSTOS).\")"

wikiup:
  hook:
    pre: $(PRINTM) cyan $@ start
    post: $(PRINTM) cyan $@ stop
  else:host: echo "'make $@' isn't yet supported on $(HOSTOS)."

```

## Template

```sh
Δ with (data=None)

export MAKEFLAGS=Δ(data['makeflags'])
include .deosrc


.DEFAULT_GOAL:=Δ(data['default_goal'])
.PHONY:Δ(data['phony'])
.SUBLIME_TARGETS:Δ(data['sublime_targets'])


all:
ifeq ($(HOSTOS),$(ISMAC))
    Δfor action in data['all']['hook']['pre']['do']: Δ(action)
    Δfor action in data['all']['if']['host']['is']['mac']['do']: Δ(action)
    Δfor action in data['all']['hook']['post']['do']: Δ(action)
else
    Δfor action in data['all']['else']['host']['do']: Δ(action)
endif


vm:
ifeq ($(HOSTOS),$(ISMAC))
    Δfor action in data['vm']['hook']['pre']['do']: Δ(action)
    Δfor action in data['vm']['if']['host']['is']['mac']['do']: Δ(action)
    Δfor action in data['vm']['hook']['post']['do']: Δ(action)
else
    Δfor action in data['vm']['else']['host']['do']: Δ(action)
endif


wiki:
ifeq ($(HOSTOS),$(ISMAC))
    Δfor action in data['wiki']['hook']['pre']['do']: Δ(action)
    Δfor action in data['wiki']['if']['host']['is']['mac']['do']: Δ(action)
    Δfor action in data['wiki']['hook']['post']['do']: Δ(action)
else
    Δfor action in data['wiki']['else']['host']['do']: Δ(action)
endif


wikiup:
ifeq ($(HOSTOS),$(ISMAC))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")
    @ (Δ(data['wikiup']['hook']['pre']))
    @-(rm -rf var/wiki)
    @ (cd var && git clone $(DeOS_GIT_REPO_WIKI) wiki)
    @ (cp meta/* var/wiki)
    @-(cd var/wiki && git add . && git commit -S -m "wiki: update" && git push)
    @-(rm -rf var/wiki)
    @ (cd var && git clone $(DeOS_GIT_REPO_WIKI) wiki)
    @ (rm -rf var/wiki/.git)
    @ (Δ(data['wikiup']['hook']['post']))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")
else
    @ (Δ(data['wikiup']['else:host']))
endif


cache:
ifeq ($(HOSTOS),$(ISMAC))
ifeq ($(SETCACHE),$(ISTRUE))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")
    @ (Δ(data['cache']['hook']['pre']))
    @-(rm -rf .cache/webpy)
    @ (cd .cache && git clone $(DeOS_GIT_REPO_WEB))
    @ (cd .cache && tar -cvzf webpy.tar.gz webpy/*)
    @ (rm -rf .cache/webpy)
    @-(rm -rf .cache/hyper)
    @ (cd .cache && git clone $(DeOS_GIT_REPO_HYPER))
    @ (cd .cache && tar -cvzf hyper.tar.gz hyper/*)
    @ (rm -rf .cache/hyper)
    @ (Δ(data['cache']['hook']['post']))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")
endif
else
    @ (Δ(data['cache']['else:host']))
endif


bips:
ifeq ($(HOSTOS),$(ISMAC))
    Δfor action in data['bips']['hook']['pre']['do']: Δ(action)
    Δfor action in data['bips']['if']['host']['is']['mac']['do']: Δ(action)
    Δfor action in data['bips']['hook']['post']['do']: Δ(action)
else
    Δfor action in data['bips']['else']['host']['do']: Δ(action)
endif


terminal:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['terminal']['hook']['pre']))
    @-(rm -rf app/terminal)
    @ (cd app && git clone $(DeOS_GIT_REPO_HYPER) terminal)
    @ (rm -rf app/terminal/.git app/terminal/.github)
    @ (Δ(data['terminal']['hook']['post']))
else
    @ (Δ(data['terminal']['else:host']))
endif


meta:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['meta']['hook']['logger']['pre']))
    @ (Δ(data['meta']['hook']['printm']['pre']))
    @ (sh bootstrap.sh)
    @ (python src/hello.py)
    $(MAKE) blockstack.clone
    $(MAKE) blockstack.venv
    Δfor cmd in data['meta']['make']: @ ($(MAKE) Δ(cmd))
    @-($(MAKE) wikiup)
    @ (Δ(data['meta']['hook']['printm']['post']))
    @ (Δ(data['meta']['hook']['logger']['post']))
else
    @ (Δ(data['meta']['else:host']))
endif


blockstack:
    source $(BASEDIR)/.deos/venv/darwin/blockstack/bin/activate && python $(BASEDIR)/src/blockstack.py whois atom.id
    source $(BASEDIR)/.deos/venv/darwin/blockstack/bin/activate && python $(BASEDIR)/src/blockstack.py wallet test

blockstack.clone:
ifeq ($(HOSTOS),$(ISMAC))
    -cd src/blockstack && rm -rf blockstack
    cd src/blockstack && git clone git@github.com:blockstack/blockstack-cli.git blockstack
    cd src/blockstack/blockstack && rm -rf .git
    -cd docs/blockstack && rm -rf blockstack_client
    mv src/blockstack/blockstack/docs docs/blockstack/blockstack_client
    mv src/blockstack/blockstack/README.md docs/blockstack/blockstack_client/README.md
    mv src/blockstack/blockstack/LICENSE docs/blockstack/blockstack_client/LICENSE
    -cd docs/blockstack && rm -rf blockstack_registrar
    mv src/blockstack/blockstack/blockstack_registrar/doc docs/blockstack/blockstack_registrar
    mv src/blockstack/blockstack/blockstack_registrar/README.md docs/blockstack/blockstack_registrar/README.md
    mv src/blockstack/blockstack/blockstack_registrar/LICENSE docs/blockstack/blockstack_registrar/LICENSE
    -cd tools/blockstack && rm -rf blockstack_client
    mv src/blockstack/blockstack/tools tools/blockstack/blockstack_client
    -cd tools/blockstack && rm -rf blockstack_registrar
    mv src/blockstack/blockstack/blockstack_registrar/tools tools/blockstack/blockstack_registrar
    -cd tests/blockstack && rm -rf blockstack_client
    cd tests/blockstack && mkdir blockstack_client
    mv src/blockstack/blockstack/unit_tests.py tests/blockstack/blockstack_client/unit_tests.py
    -cd tests/blockstack && rm -rf blockstack_registrar
    mv src/blockstack/blockstack/blockstack_registrar/tests tests/blockstack/blockstack_registrar

    -rm -rf tests/blockstack/integration
    #cd tests/blockstack && git clone git@github.com:blockstack/blockstack-integration-tests.git integration
    #rm -rf tests/blockstack/integration/.git

    -rm -rf src/blockstack/keychain
    cd src/blockstack && git clone git@github.com:blockstack/keychain-manager-py.git keychain
    rm -rf src/blockstack/keychain/.git
    -rm -rf docs/blockstack/keychain
    mkdir docs/blockstack/keychain
    mv src/blockstack/keychain/LICENSE docs/blockstack/keychain/LICENSE
    mv src/blockstack/keychain/README.md docs/blockstack/keychain/README.md
    -rm -rf tests/blockstack/keychain
    mkdir tests/blockstack/keychain
    mv src/blockstack/keychain/unit_tests.py tests/blockstack/keychain/unit_tests.py

    -rm -rf src/blockstack/keylib
    cd src/blockstack && git clone git@github.com:blockstack/keylib-py.git keylib
    rm -rf src/blockstack/keylib/.git
    -rm -rf docs/blockstack/keylib
    mkdir docs/blockstack/keylib
    mv src/blockstack/keylib/LICENSE docs/blockstack/keylib/LICENSE
    mv src/blockstack/keylib/README.md docs/blockstack/keylib/README.md
    -rm -rf tests/blockstack/keylib
    mkdir tests/blockstack/keylib
    mv src/blockstack/keylib/unit_tests.py tests/blockstack/keylib/unit_tests.py

    -rm -rf src/blockstack/virtualchain
    cd src/blockstack && git clone git@github.com:blockstack/virtualchain.git
    rm -rf src/blockstack/virtualchain/.git
    -rm -rf docs/blockstack/virtualchain
    mkdir docs/blockstack/virtualchain
    mv src/blockstack/virtualchain/LICENSE docs/blockstack/virtualchain/LICENSE
    mv src/blockstack/virtualchain/README.md docs/blockstack/virtualchain/README.md
    mv src/blockstack/virtualchain/virtualchain/impl_ref docs/blockstack/virtualchain/impl_ref

    -cd src/blockstack && rm -rf pybitcoin
    cd src/blockstack && git clone git@github.com:blockstack/pybitcoin.git
    cd src/blockstack/pybitcoin && rm -rf .git
    -cd tests/blockstack && rm -rf pybitcoin
    mv src/blockstack/pybitcoin/tests tests/blockstack/pybitcoin
    mv src/blockstack/pybitcoin/unit_tests.py tests/blockstack/pybitcoin/unit_tests.py
    -cd docs/blockstack && rm -rf pybitcoin
    mkdir docs/blockstack/pybitcoin
    mv src/blockstack/pybitcoin/AUTHORS docs/blockstack/pybitcoin/AUTHORS
    mv src/blockstack/pybitcoin/DEPRECATED.md docs/blockstack/pybitcoin/DEPRECATED.md
    mv src/blockstack/pybitcoin/LICENSE docs/blockstack/pybitcoin/LICENSE
    mv src/blockstack/pybitcoin/README.md docs/blockstack/pybitcoin/README.md
    mv src/blockstack/pybitcoin/MANIFEST.in docs/blockstack/pybitcoin/MANIFEST.in
endif


blockstack.venv:
ifeq ($(HOSTOS),$(ISMAC))
    -([ -d "$(BASEDIR)/.deos/venv/darwin/blockstack" ] && rm -rf $(BASEDIR)/.deos/venv/darwin/blockstack)
    cd $(BASEDIR)/.deos/venv/darwin && virtualenv blockstack --no-site-packages
    source $(BASEDIR)/.deos/venv/darwin/blockstack/bin/activate && pip install blockstack && pip install simplejson && pip install ruamel.yaml
endif


pycpp:
ifeq ($(HOSTOS),$(ISMAC))
    -cd src && rm -rf pypreprocessor
    cd src && git clone git@github.com:evanplaice/pypreprocessor.git
    cd src/pypreprocessor && rm -rf .git
    -rm tests/pypreprocessor test.py
    mv src/pypreprocessor/test.py tests/pypreprocessor/test.py
    -rm -rf docs/pypreprocessor
    mkdir docs/pypreprocessor
    mv src/pypreprocessor/Examples docs/pypreprocessor/examples
    mv src/pypreprocessor/LICENSE docs/pypreprocessor/LICENSE
    mv src/pypreprocessor/INSTALL.md docs/pypreprocessor/INSTALL.md
    mv src/pypreprocessor/README.md docs/pypreprocessor/README.md
    mv src/pypreprocessor/MANIFEST docs/pypreprocessor/MANIFEST
endif


webpy:
ifeq ($(HOSTOS),$(ISMAC))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 0")
    @ (Δ(data['webpy']['hook']['pre']))
    @-(rm -rf src/web/)
ifeq ($(USECACHE),$(ISTRUE))
    @-(rm src/web.tar)
    @ ([ -f ".cache/webpy.tar.gz" ] && Δ(data['webpy']['if:repo;is:cached']) || Δ(data['webpy']['else:repo']))
    @-(rm src/web.tar)
else
    @ (cd src/ && git clone $(DeOS_GIT_REPO_WEB) web)
endif
    @ (rm -rf src/web/.git)
    @-(rm src/web/.gitignore)
    @-(rm src/web/.travis.yml)
    @-(rm -rf tools/web)
    @ (mv src/web/tools tools/web)
    @ (mv src/web/test tests/web)
    @ (mv src/web/docs docs/web)
    @ (mv src/web/LICENSE.txt docs/web/LICENSE.txt)
    @ (mv src/web/ChangeLog.txt docs/web/ChangeLog.txt)
    @ (mv src/web/README.md docs/web/README.md)
    @ (Δ(data['webpy']['hook']['post']))
    @ ($(LOGGER) "INFO" "$(HOSTOS) : make : $@ : 1")
else
    @ Δ(data['webpy']['else:host'])
endif


clean:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['clean']['hook']['pre']))
    @ ([ -d ".deos" ] && $(DeOS_RM_DOTDEOS) || echo "$@:else")
    @ (Δ(data['clean']['hook']['post']))
else
    @ (Δ(data['clean']['else:host']))
endif


install:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['install']['hook']['pre']))
    @ ([ ! -x "$(DeOS_BIN_TRAVIS)" ] && $(DeOS_ADD_TRAVIS) || echo "$@:else")
    @ (Δ(data['install']['hook']['post']))
else
    @ (Δ(data['install']['else:host']))
endif


build:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['build']['hook']['pre']))
    @ ([ ! -d ".deos" ] && $(DeOS_ADD_DOTDEOS) || echo "$@:else")
    @ (Δ(data['build']['hook']['post']))
else
    @ (Δ(data['build']['else:host']))
endif


venv:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['venv']['hook']['pre']))
    @ ([   -d ".deos/venv" ] && rm -rf .deos/venv || echo "$@:else")
    @ ([ ! -d ".deos/venv" ] && mkdir .deos/venv .deos/venv/darwin .deos/venv/vagrant .deos/venv/travis || echo "$@:else")
    @ (Δ(data['venv']['hook']['post']))
else
    @ Δ(data['venv']['else:host'])
endif


lint:
ifeq ($(HOSTOS),$(ISMAC))
    @ (Δ(data['lint']['hook']['pre']))
    @ (Δ(data['lint']['if:host;is:mac']))
    @ (Δ(data['lint']['hook']['post']))
else
    @ (Δ(data['lint']['else:host']))
endif
```

## Test

```yaml
a: 1
b: 2
c: 3
```
