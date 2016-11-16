vagrant: vagrant.down vagrant.up

vagrant.ssh:
	cd $(PATH_BASE) && vagrant ssh

vagrant.down:
	-cd $(PATH_BASE) && vagrant destroy

vagrant.up: $(PATH_BASE)/Vagrantfile
	-cd $(PATH_BASE) && vagrant up

$(PATH_BASE)/Vagrantfile: $(PATH_BASE)/.vagrant
	-cd $(PATH_BASE) && vagrant init osx

$(PATH_BASE)/.vagrant:
	-rm -rf $(PATH_BASE)/.vagrant/
	-rm $(PATH_BASE)/Vagrantfile
