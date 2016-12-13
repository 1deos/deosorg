# -*- mode: ruby -*-
# vi: set ft=ruby :

require './src/boot/plugins/vagrant-provision-reboot-plugin'

Vagrant.configure('2') do |config|

  config.vm.define :DeVM do |t| end
  config.vm.box = ENV['DeOS_VMBOX']
  config.vm.box_check_update = true

  config.ssh.paranoid = true
  if ARGV[0] == 'ssh' ? config.ssh.shell = ENV['VM_SHELL_SSH']
                      : config.ssh.shell = ENV['VM_SHELL']
  end

  if ENV['DeOS_RUNSERVER'] != '0'
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
    config.vm.synced_folder '.', ENV['VM_PATH']
    config.vm.synced_folder '.zerotier', ENV['VM_PATH_ZT'],
      owner: 'root',
      group: 'root',
    create: true
  end # file_sync

  #config.vm.provision :shell,
  #  env: {
  #    'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
  #    'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG'],
  #    'DeOS_BUILD_APT_UPGRADE' => ENV['DeOS_BUILD_APT_UPGRADE']
  #  },
  #  path: ENV['DeOS_BOOT_SCRIPT'],
  #:args => ENV['DeOS_BOOT_ARGS_BOOTSTRAP']

  #config.vm.provision :unix_reboot

  if ENV['DeOS_BUILD_BITCOIN'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args => ENV['DeOS_BOOT_ARGS_BITCOIN']
  end # bitcoin

  if ENV['BUILDZT'] != '0'
    config.vm.provision :shell, # zerotier
                    path:ENV['VM_BOOT'],
                     env:{'ZT_GPG_KEY'=>ENV['ZT_GPG_KEY'],
                          'ZT_INSTALL'=>ENV['ZT_INSTALL'],
                          'ZT_INSTALL_TMP'=>ENV['ZT_INSTALL_TMP'],
                          'ZT_NETWORK'=>ENV['ZT_NETWORK']},
                        :args=>'-v'
  end # BUILDZT

  if ENV['BUILDNGINX'] != '0'
    config.vm.provision :shell, # nginx
                    path:ENV['VM_BOOT'],
                     env:{'BOOT_DEBUG'=>ENV['BOOT_DEBUG']},
                        :args=>'-x'
  end # BUILDNGINX

  if ENV['BUILDJS'] != '0'
    config.vm.provision :shell, # nodejs
                    path:ENV['VM_BOOT'],
                     env:{'BOOT_DEBUG'=>ENV['BOOT_DEBUG'],
                          'NODE_INSTALL'=>ENV['NODE_INSTALL']},
                        :args=>'-n'

    config.vm.provision :shell, # nvm
                    path:ENV['VM_BOOT'],
                     env:{'NVM_GIT_REPO'=>ENV['NVM_GIT_REPO'],
                          'VM_PATH'=>ENV['VM_PATH'],
                          'VM_PATH_NVM'=>ENV['VM_PATH_NVM']},
                        :args=>'-u'

    #config.vm.provision :shell, # yarn
                    #path:ENV['VM_BOOT'],
                        #:args=>'-y'
  end # BUILDJS

  if ENV['DeOS_BUILD_PYTHON'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG']
      },
      path:ENV['VM_BOOT'],
    :args=>ENV['DeOS_BOOT_ARGS_PYTHON']
    #config.vm.provision :shell, # virtualenv
                    #path:ENV['VM_BOOT'],
                        #:args=>'-r'
  end # python

  if ENV['DeOS_BUILD_BLOCKSTACK'] != '0' && ENV['DeOS_BUILD_PYTHON'] != '0'
    config.vm.provision :shell,
      env: {
        'DeOS_BOOT_PATH' => ENV['DeOS_BOOT_PATH'],
        'DeOS_BOOT_DEBUG' => ENV['DeOS_BOOT_DEBUG']
      },
      path: ENV['DeOS_BOOT_SCRIPT'],
    :args => ENV['DeOS_BOOT_ARGS_BLOCKSTACK']
  end # blockstack

  if ENV['BUILDDOCKER'] != '0'
    config.vm.provision :shell, # docker
                    path:ENV['VM_BOOT'],
                     env:{'BOOT_DEBUG'=>ENV['BOOT_DEBUG'],
                          'DOCKER_APT_REPO'=>ENV['DOCKER_APT_REPO'],
                          'DOCKER_GPG_KEY'=>ENV['DOCKER_GPG_KEY'],
                          'DOCKER_KEY_SERV'=>ENV['DOCKER_KEY_SERV'],
                          'DOCKER_SOURCES'=>ENV['DOCKER_SOURCES'],
                          'DOCKER_UBUNTU'=>ENV['DOCKER_UBUNTU'],
                          'UBUNTU_GPG_KEY'=>ENV['UBUNTU_GPG_KEY'],
                          'UBUNTU_KEY_SERV'=>ENV['UBUNTU_KEY_SERV']},
                        :args=>'-w'

    config.vm.provision :unix_reboot

    config.vm.provision :shell, # dvm
              privileged:false,
                    path:ENV['VM_BOOT'],
                     env:{'DOCKER_VERSION'=>ENV['DOCKER_VERSION'],
                          'DVM_ACTIVATE'=>ENV['DVM_ACTIVATE'],
                          'DVM_INSTALL'=>ENV['DVM_INSTALL'],
                          'VM_BASHRC'=>ENV['VM_BASHRC']},
                        :args=>'-m'

    config.vm.provision :shell, # compose
                    path:ENV['VM_BOOT'],
                        :args=>'-z'

    config.vm.provision :shell, # flask
                    path:ENV['VM_BOOT'],
                     env:{'DOCKER_PY_PATH'=>ENV['DOCKER_PY_PATH']},
                        :args=>'-f'
  end # BUILDDOCKER

  if ENV['BUILDNOTEBOOK'] != '0'
    config.vm.provision :shell, # jupyter
                    path:ENV['VM_BOOT'],
                        :args=>'-j'
  end # BUILDNOTEBOOK

end # Vagrant.configure('2') do |config|
