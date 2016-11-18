# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :forwarded_port, guest:80, host:4567
  config.vm.network :forwarded_port, guest:8888, host:8888
  config.vm.provision :shell, inline:<<-SHELL
    apt-get update
    apt-get install -y build-essential
    apt-get install -y libffi-dev
    apt-get install -y libssl-dev
  SHELL
  config.vm.provision :shell, inline:<<-SHELL
    sudo apt-get install -y nginx
    rm /etc/nginx/nginx.conf
    ln -s /vagrant/etc/nginx/nginx.conf /etc/nginx/nginx.conf
    if ! [ -L /etc/nginx/sites-available/default ]; then
      rm -rf /etc/nginx/sites-available/default
      ln -s /vagrant/etc/nginx/sites-available/deos.conf \
            /etc/nginx/sites-available/deos.conf
    fi
  SHELL
  config.vm.provision :shell, inline:<<-SHELL
    apt-get install -y python2.7
    apt-get install -y python-pip
    apt-get install -y python-dev
    apt-get install -y ipython
    apt-get install -y ipython-notebook
    pip install --upgrade pip
    pip install --upgrade pyopenssl
    pip install ndg-httpsclient
    pip install pyasn1
    pip install --upgrade requests[security]
    pip install jupyter
    pip install ipyparallel
    ipcluster nbextension enable
  SHELL
  config.vm.provision :shell, privileged:false, inline:<<-SHELL
    ipython profile create vagrant
    if ! [ -L /home/vagrant/.ipython/profile_vagrant/ipython_config.py ]; then
      rm /home/vagrant/.ipython/profile_vagrant/ipython_config.py
      ln -s /vagrant/etc/ipython/ipython_config.py \
            /home/vagrant/.ipython/profile_vagrant/ipython_config.py
    fi
  SHELL
  config.vm.provision :shell, privileged:false, inline:<<-SHELL
    cd /home/vagrant
    wget -qO- https://raw.github.com/creationix/nvm/v0.32.1/install.sh | sh
    export NVM_DIR="/home/vagrant/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
    cd /vagrant && nvm install && nvm use
  SHELL
  config.vm.provision :shell, privileged:false, run:"always", inline:<<-SHELL
    jupyter notebook --notebook-dir=/vagrant/var/notebook \
                     --no-browser \
                     --ip=0.0.0.0 &
  SHELL
end
