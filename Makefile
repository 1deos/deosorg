include .deosrc

.DEFAULT_GOAL := all
.PHONY: all build docs.build docs.start graphviz wikid push run sync venv \
	wiki.pull wiki.push
.SUBLIME_TARGETS: all

all:
	@-$(MAKE) build
	@-$(MAKE) run

build:
	@-$(MAKE) venv
	@-$(MAKE) docs.build

docs.build:
	@-$(CD) docs && $(MAKE) build

docs.start:
	$(MAKE) docs.build
	@-$(CD) docs && $(MAKE)

graphviz:
	@-$(ACTVENV) && $(CD) src && $(PY) graphviz.py
	@-dot -Tpng var/dot/g.dot > var/img/g.png

#wikid:
	#@$(CD) meta/wikid && $(MAKE)

push:
	@-$(GITADD) && $(GITCOMMIT) "$(msg)" && $(GITPUSH)

run:
	@-$(MAKE) graphviz

sync:
	@-$(MAKE) wiki.pull
	@-$(MAKE) msg="make sync" push

venv:
	@-$(RM) $(DOTVENV)
	@-$(MKDIR) $(DOTVENV)
	@-$(VENV) $(DOTVENV)
	@-$(ACTVENV) && $(PIPINSTALL) -r $(PYREQ)

wiki.pull:
	@-$(RM) $(VARWIKI)
	@-$(CD) $(VAR) && $(GITCLONE) $(COREWIKI) wiki
	@-$(RM) $(VARWIKI)/.git
	@#$(RM) meta/wikid/static/
	@#$(MKDIR) meta/wikid/static/
	@#$(CD) meta/wikid/static && $(GITCLONE) $(COREWIKI) .
	@#$(RM) meta/wikid/static/.git

wiki.push:
	@-$(RM) $(DOTSWAP)
	@-$(MKDIR) $(DOTSWAP)
	@-$(CD) $(DOTSWAP) && $(GITCLONE) $(COREWIKI) wiki
	@-$(RM) $(SWAPWIKI)/*.md
	@-$(CP) $(VARWIKI)/*.md $(SWAPWIKI)/
	@-$(CD) $(SWAPWIKI) && mkdir img
	@-$(CP) -a $(VARWIKI)/img/. $(SWAPWIKI)/img/
	@-$(CD) $(SWAPWIKI) && $(GITADD) && $(GITCOMMIT) "$(WIKIMSG)" && $(GITPUSH)
	@-$(RM) $(DOTSWAP)

#[endfi]
