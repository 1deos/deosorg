[this:author:name]:  # (Andrew DeSantis)
[this:author:email]: # (atd@bitcoin.sh)

---

# [ΔOS v0.8-alpha.9][000] | `deos-core` | [![Build Status][001]][002]

[![self-header.jpg][003]](https://github.com/libdeos/deos-graphviz/wiki)

---

> *The languages of intelligence (writing) and self-interest (money) are the*
> *mind's greatest creations; both must be decentralized or all is lost.*
> **[—DeSantis][004]**

---

## Commands

* `make all`
* `make build`
* `make clean`
* `make docs.build`
* `make docs.start`
* `make graphviz`
* `make msg="add: var/asset/img/*.png" push`
* `make run`
* `make sync`
* `make venv`
* `make wiki.pull`
* `make wiki.push`
* `make wikid`

---

## `.env` Example

```bash
include src/make/deos.mk
export MAKEFLAGS := --no-print-directory
VOLUME           := /example/example
VOLMOD           := example/example/example
V                := $(VOLUME)/$(VOLMOD)
#[endfi]
```

---

[000]: https://libdeos.github.io/deos-graphviz/
[001]: https://travis-ci.org/libdeos/deos-graphviz.svg?branch=master
[002]: https://travis-ci.org/libdeos/deos-graphviz
[003]: var/assets/github/self-header.jpg
[004]: https://twitter.com/desantis/status/795023340704595968
