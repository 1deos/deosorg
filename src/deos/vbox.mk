vm.down:; ([ -d $(BASEDIR)/.vagrant/ ] && vagrant destroy DeVM --force)

vm.install:; ([ ! -d $(BASEDIR)/.vagrant/ ] && vagrant up --provider virtualbox)

vm.ssh:; (vagrant ssh -c $(VMCMD) DeVM)

vm.uninstall: vm.down
	-rm $(BASEDIR)/app/index.min.html
	-rm -rf $(BASEDIR)/.vagrant/
	-rm -rf $(BASEDIR)/app/node_modules/
	-rm -rf $(BASEDIR)/node_modules/
