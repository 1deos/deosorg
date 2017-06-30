# -*- mode: ruby -*-
# vi: set ft=ruby :

require './src/reboot'
Vagrant.configure("2") do |config|
  config.vm.define :DeVM do |t| end
  config.vm.box = ENV['DeOS_VM_BOX']
  config.vm.box_check_update = true
  config.ssh.paranoid = true
  if ARGV[0] == 'ssh' ? config.ssh.shell = ENV['DeOS_VM_SHELL_SSH']
                      : config.ssh.shell = ENV['DeOS_VM_SHELL_DEFAULT']
  end # set_shell()
  config.vm.provision :shell, inline:<<-SHELL
    apt-get update
    apt-get install -y build-essential
  SHELL
  config.vm.provision :unix_reboot
end # Vagrant.configure('2') do |config|
