# `Vagrantfile`

## Schema

```yaml
type: object
required: [a, b, c]
properties:
  a: {type: number}
  b: {type: number}
  c: {type: number}
```

## Environment

```yaml
a: 1
b: 2
c: 3
```

## Template

```ruby
Δ with (data=None)
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
  if ENV['DeOS_BUILD_BITCOIN'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
        'DeOS_CMD_APT_UPGRADE' => ENV['DeOS_CMD_APT_UPGRADE']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args => ENV['DeOS_BOOT_ARGS_BITCOIN']
  end # bitcoin
  if ENV['BUILDZT'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
        'DeOS_CMD_APT_UPGRADE' => ENV['DeOS_CMD_APT_UPGRADE'],
        'ZT_GPG_KEY' => ENV['ZT_GPG_KEY'],
        'ZT_INSTALL' => ENV['ZT_INSTALL'],
        'ZT_INSTALL_TMP' => ENV['ZT_INSTALL_TMP'],
        'ZT_NETWORK' => ENV['ZT_NETWORK']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args=>'-v'
  end # zerotier
  ###
  if ENV['DeOS_BUILD_NGINX'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args => ENV['DeOS_BOOT_ARGS_NGINX']
  end # nginx
  ###
  if ENV['BUILDJS'] != '0'
    config.vm.provision :shell,
      env: {
        'BOOT_DEBUG' => ENV['BOOT_DEBUG'],
        'NODE_INSTALL' => ENV['NODE_INSTALL']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args=>'-n' # node
    config.vm.provision :shell,
      env: {
        'NVM_GIT_REPO' => ENV['NVM_GIT_REPO'],
        'VM_PATH' => ENV['VM_PATH'],
        'VM_PATH_NVM' => ENV['VM_PATH_NVM']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args=>'-u' # nvm
    #config.vm.provision :shell,
      #path: ENV['DeOS_BOOT_SCRIPT'],
    #:args => '-y' # yarn
  end # nodejs
  if ENV['DeOS_BUILD_PYTHON'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
        'DeOS_CMD_APT_UPGRADE' => ENV['DeOS_CMD_APT_UPGRADE']
      },
      path:ENV['DeOS_BOOT_SCRIPT'],
    :args=>ENV['DeOS_BOOT_ARGS_PYTHON']
    if ENV['DeOS_BUILD_BLOCKSTACK'] != '0'
      config.vm.provision :shell,
        env: {
          'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
          'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG']
        },
        path: ENV['DeOS_BOOT_SCRIPT'],
        privileged: false,
      :args => ENV['DeOS_BOOT_ARGS_BLOCKSTACK']
    end # blockstack
    if ENV['BUILDNOTEBOOK'] != '0'
      config.vm.provision :shell,
        path: ENV['DeOS_BOOT_SCRIPT'],
      :args=>'-j'
    end # jupyter
  end # python
  if ENV['BUILDDOCKER'] != '0'
    config.vm.provision :shell,
      env: {
        'BOOT_DEBUG' => ENV['BOOT_DEBUG'],
        'DOCKER_APT_REPO' => ENV['DOCKER_APT_REPO'],
        'DOCKER_GPG_KEY' => ENV['DOCKER_GPG_KEY'],
        'DOCKER_KEY_SERV' => ENV['DOCKER_KEY_SERV'],
        'DOCKER_SOURCES' => ENV['DOCKER_SOURCES'],
        'DOCKER_UBUNTU' => ENV['DOCKER_UBUNTU'],
        'UBUNTU_GPG_KEY' => ENV['UBUNTU_GPG_KEY'],
        'UBUNTU_KEY_SERV' => ENV['UBUNTU_KEY_SERV']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args=>'-w'
    config.vm.provision :unix_reboot
    config.vm.provision :shell,
      env: {
        'DOCKER_VERSION' => ENV['DOCKER_VERSION'],
        'DVM_ACTIVATE' => ENV['DVM_ACTIVATE'],
        'DVM_INSTALL' => ENV['DVM_INSTALL'],
        'VM_BASHRC' => ENV['VM_BASHRC']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
      privileged: false,
    :args=>'-m' # dvm
    config.vm.provision :shell,
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args => '-z' # compose
    config.vm.provision :shell,
      env: {
        'DOCKER_PY_PATH' => ENV['DOCKER_PY_PATH']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args=>'-i' # flask
  end # docker
end # Vagrant.configure('2') do |config|
```

## Test: Environment

```yaml
a: 1
b: 2
c: 3
```

## Test: Pass

```sh
#!/bin/sh
echo "1"
echo "2"
echo "3"
```

## Test: Fail

```sh
#!/bin/sh
echo "3"
echo "2"
echo "1"
```
