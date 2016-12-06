vm.down:; ([ -d $(BASEDIR)/.vagrant/ ] && vagrant destroy DeVM --force)

vm.install:; ([ ! -d $(BASEDIR)/.vagrant/ ] && $(DELTA) $(UPCMD))

vm.ssh:; (vagrant ssh -c $(VMCMD) DeVM)

vm.uninstall: vm.down
	chmod +x $(BASEDIR)/bin/delta
	-rm $(BASEDIR)/app/index.min.html
	-rm -rf $(BASEDIR)/.zerotier/
	-rm -rf $(BASEDIR)/.vagrant/
	-rm -rf $(BASEDIR)/app/node_modules/
	-rm -rf $(BASEDIR)/node_modules/
	-rm -rf $(BASEDIR)/var/docker/nginx/ \
		&& mkdir $(BASEDIR)/var/docker/nginx/ \
		&& cp $(BASEDIR)/var/templates/gitignore.txt \
		      $(BASEDIR)/var/docker/nginx/.gitignore
	-rm -rf $(BASEDIR)/var/docker/python/ \
		&& mkdir $(BASEDIR)/var/docker/python/ \
		&& cp $(BASEDIR)/var/templates/gitignore.txt \
		      $(BASEDIR)/var/docker/python/.gitignore
