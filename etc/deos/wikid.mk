wikid: $(PATH_WIKI)
	@$(MAKE) wikid.push

$(PATH_WIKI):
	@$(MAKE) wikid.pull

wikid.pull:
	@$(PRINT) yellow $@ start
	-rm -rf $(PATH_WIKI)/
	cd $(PATH_TMP) && find . ! -name '.gitignore' -delete
	cd $(PATH_TMP) && git clone git@github.com:desantis/DeOS.wiki.git
	rm -rf $(PATH_TMP)/DeOS.wiki/.git/
	mv $(PATH_TMP)/DeOS.wiki/ $(PATH_WIKI)/
	@$(PRINT) yellow $@ stop

wikid.push:
	@$(PRINT) purple $@ start
	cd $(PATH_TMP) && find . ! -name '.gitignore' -delete
	cd $(PATH_TMP) && git clone git@github.com:desantis/DeOS.wiki.git
	mv $(PATH_TMP)/DeOS.wiki/.git/ $(PATH_WIKI)/.git/
	rm -rf $(PATH_TMP)/DeOS.wiki/
	mkdir $(PATH_TMP)/DeOS.wiki/
	mv $(PATH_WIKI)/.git/ $(PATH_TMP)/DeOS.wiki/.git/
	mv -v $(PATH_WIKI)/* $(PATH_TMP)/DeOS.wiki/
	-cd $(PATH_TMP)/DeOS.wiki\
	&& git status\
	&& git add .\
	&& git commit -m "wikid: push"\
	&& git push
	@$(PRINT) purple $@ stop
	@$(MAKE) wikid.pull
