# -*- mode: ruby -*-
# vi: set ft=ruby :

require './src/devm/plugins/vagrant-provision-reboot-plugin'

Vagrant.configure("2") do |config|
  config.vm.define :DeVM do |t| end
  config.vm.box = ENV['VM_BOX']
  config.vm.box_check_update = true
  config.ssh.paranoid = true
  config.ssh.shell = ENV['VM_SHELL']
  config.vm.network :forwarded_port,
    guest:ENV['VM_GUEST'],
    host:ENV['VM_HOST']
  config.vm.network :forwarded_port,
    guest:5000,
    host:1335
  config.vm.network :forwarded_port,
    guest:8888,
    host:1336
  config.vm.synced_folder ".", "/vagrant",
    disabled:true
  config.vm.synced_folder ".", ENV['VM_PATH']
  config.vm.synced_folder ".zerotier/", "/var/lib/zerotier-one",
    owner:"root",
    group:"root",
    create:true
  config.vm.provision :shell, # common
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-c"
  config.vm.provision :unix_reboot
  config.vm.provision :shell, # zerotier
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "v"
  config.vm.provision :shell, # nginx
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-x"
  config.vm.provision :shell, # nodejs
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-n"
  config.vm.provision :shell, # nvm
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-u"
  config.vm.provision :shell, # yarn
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-y"
  config.vm.provision :shell, # python
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-p"
  config.vm.provision :shell, # docker
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-d"
  config.vm.provision :unix_reboot
  config.vm.provision :shell, # dvm
    privileged:false,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-b"
  config.vm.provision :shell, # compose
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-z"
  config.vm.provision :shell, # flask
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-f"
  config.vm.provision :shell, # jupyter
    privileged:true,
    path:ENV['VM_BOOTSTRAP'],
    :args => "-j"
end
