vm.down:
	[ -d $(BASEDIR)/.vagrant/ ] && vagrant destroy DeVM --force

vm.update:
	-vagrant box update --box bento/ubuntu-16.04

vm.install:
	[ ! -d $(BASEDIR)/.vagrant/ ] && $(DELTA) $(UPCMD)

vm.ssh:
	vagrant ssh -c $(VMCMD) DeVM

vm.uninstall: vm.down
	chmod +x $(BASEDIR)/bin/delta
	-rm $(BASEDIR)/app/index.min.html
	-rm -rf $(BASEDIR)/app/node_modules/
	-rm -rf $(BASEDIR)/node_modules/
	-rm -rf $(BASEDIR)/static/docker/nginx/ \
		&& mkdir $(BASEDIR)/static/docker/nginx/ \
		&& cp $(BASEDIR)/static/templates/gitignore.txt \
		      $(BASEDIR)/static/docker/nginx/.gitignore
	-rm -rf $(BASEDIR)/static/docker/python/ \
		&& mkdir $(BASEDIR)/static/docker/python/ \
		&& cp $(BASEDIR)/static/templates/gitignore.txt \
		      $(BASEDIR)/static/docker/python/.gitignore
