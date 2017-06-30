# `Vagrantfile`

## Schema

```yaml
type: object
required: [config, plugins]
properties:


  config:
    type: object
    required: [box, ssh, vm]
    properties:


      box:
        type: object
        required: [check_update, name]
        properties:
          check_update: {type: string}
          name: {type: string}


      ssh:
        type: object
        required: [paranoid, shell]
        properties:
          paranoid: {type: string}


          shell:
            type: object
            required: [default, ssh]
            properties:
              default: {type: string}
              ssh: {type: string}

      vm:
        type: object
        required: [name]
        properties:
          name: {type: string}


  plugins:
    type: object
    required: [reboot]
    properties:
      reboot: {type: string}
```

## Environment

```yaml
config:

  box:
    check_update: 'true'
    name: ENV['DeOS_VM_BOX']

  vm:
    name: DeVM

  ssh:
    paranoid: 'true'
    shell:
      default: ENV['DeOS_VM_SHELL_DEFAULT']
      ssh: ENV['DeOS_VM_SHELL_SSH']

plugins:
  reboot: ./src/vagrant/reboot
```

## Template

```ruby
Δ with (data=None)
# -*- mode: ruby -*-
# vi: set ft=ruby :


require 'Δ(data['plugins']['reboot'])'
Vagrant.configure('2') do |config|


  config.vm.define :Δ(data['config']['vm']['name']) do |t| end
  config.vm.box = Δ(data['config']['box']['name'])
  config.vm.box_check_update = Δ(data['config']['box']['check_update'])


  config.ssh.paranoid = Δ(data['config']['ssh']['paranoid'])
  if ARGV[0] == 'ssh' ? config.ssh.shell = Δ(data['config']['ssh']['shell']['ssh'])
                      : config.ssh.shell = Δ(data['config']['ssh']['shell']['default'])
  end # set_shell


  #if ENV['DeOS_RUN_SERVER'] != '0'
  #  config.vm.network :forwarded_port,
  #    guest: ENV['DeOS_VM_PORT_GUEST_0'],
  #    host: ENV['DeOS_VM_PORT_HOST_0']
  #  config.vm.network :forwarded_port,
  #    guest: ENV['DeOS_VM_PORT_GUEST_1'],
  #    host: ENV['DeOS_VM_PORT_HOST_1']
  #  config.vm.network :forwarded_port,
  #    guest: ENV['DeOS_VM_PORT_GUEST_2'],
  #    host: ENV['DeOS_VM_PORT_HOST_2']
  #end # run_server


  #if ENV['DeOS_FILESYNC'] != '0'
  #  config.vm.synced_folder '.', '/vagrant',
  #    disabled: true
  #  config.vm.synced_folder '.', ENV['DeOS_VM_PATH']
  #  config.vm.synced_folder 'etc/zerotier', ENV['DeOS_VM_PATH_ZT'],
  #    owner: 'root',
  #    group: 'root',
  #  create: true
  #  config.vm.synced_folder 'etc/blockstack', '/home/vagrant/.blockstack',
  #    owner: 'vagrant',
  #    group: 'vagrant',
  #  create: true
  #end # file_sync


  #config.vm.provision :shell,
  #  env: {
  #    'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
  #    'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
  #    'DeOS_BUILD_APT_UPGRADE' => ENV['DeOS_BUILD_APT_UPGRADE'],
  #    'DeOS_CMD_APT_UPGRADE' => ENV['DeOS_CMD_APT_UPGRADE']
  #  },
  #  path: ENV['DeOS_BOOT_SCRIPT'],
  #:args => ENV['DeOS_BOOT_ARGS_BOOTSTRAP']
  config.vm.provision :unix_reboot
  #end # bitcoin


end # Vagrant.configure('2') do |config|
```

## Test

```yaml
a: 1
b: 2
c: 3
```
