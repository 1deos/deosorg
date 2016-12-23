# -*- mode: ruby -*-
# vi: set ft=ruby :
require './src/vagrant/reboot'
Vagrant.configure('2') do |config|
  config.vm.define :DeVM do |t| end
  config.vm.box = ENV['DeOS_VM_BOX']
  config.vm.box_check_update = true
  config.ssh.paranoid = true
  if ARGV[0] == 'ssh' ? config.ssh.shell = ENV['DeOS_VM_SHELL_SSH']
					  : config.ssh.shell = ENV['DeOS_VM_SHELL_DEFAULT']
  end # set_shell
  if ENV['DeOS_RUN_SERVER'] != '0'
	config.vm.network :forwarded_port,
	  guest: ENV['DeOS_VM_PORT_GUEST_0'],
	  host: ENV['DeOS_VM_PORT_HOST_0']
	config.vm.network :forwarded_port,
	  guest: ENV['DeOS_VM_PORT_GUEST_1'],
	  host: ENV['DeOS_VM_PORT_HOST_1']
	config.vm.network :forwarded_port,
	  guest: ENV['DeOS_VM_PORT_GUEST_2'],
	  host: ENV['DeOS_VM_PORT_HOST_2']
  end # run_server
  if ENV['DeOS_FILESYNC'] != '0'
	config.vm.synced_folder '.', '/vagrant',
	  disabled: true
	config.vm.synced_folder '.', ENV['DeOS_VM_PATH']
	config.vm.synced_folder 'etc/zerotier', ENV['DeOS_VM_PATH_ZT'],
	  owner: 'root',
	  group: 'root',
	create: true
	config.vm.synced_folder 'etc/blockstack', '/home/vagrant/.blockstack',
	  owner: 'vagrant',
	  group: 'vagrant',
	create: true
  end # file_sync
  config.vm.provision :shell,
	env: {
	  'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
	  'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
	  'DeOS_BUILD_APT_UPGRADE' => ENV['DeOS_BUILD_APT_UPGRADE'],
	  'DeOS_CMD_APT_UPGRADE' => ENV['DeOS_CMD_APT_UPGRADE']
	},
	path: ENV['DeOS_BOOT_SCRIPT'],
  :args => ENV['DeOS_BOOT_ARGS_BOOTSTRAP']
  config.vm.provision :unix_reboot
  end # bitcoin
end # Vagrant.configure('2') do |config|
