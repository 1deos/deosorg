# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.network :forwarded_port, guest:80, host:1337

  config.vm.network :forwarded_port, guest:8888, host:1321

  config.vm.define :DeVM do |t| end

  config.vm.provision :shell, inline:<<-SHELL
    apt-get update
    apt-get install -y build-essential
    apt-get install -y llvm
    apt-get install -y clang-3.4
    apt-get install -y ntp
    apt-get install -y libffi-dev
    apt-get install -y libssl-dev
    apt-get install -y apt-transport-https
    apt-get install -y ca-certificates
    apt-get install -y git
  SHELL

  config.vm.provision :shell, inline:<<-SHELL
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 \
                --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
    echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" \
      | tee /etc/apt/sources.list.d/docker.list
    apt-get update
    apt-get install -y linux-image-extra-$(uname -r) \
                       linux-image-extra-virtual
    apt-get install -y docker-engine
    sudo service docker start
    sudo docker run hello-world
    sudo groupadd docker
    sudo usermod -aG docker $USER
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
    sudo service nginx reload
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
    pip install docker-compose
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
    cd /vagrant && nvm install \
                && nvm use \
                && npm install --global yarn \
                && yarn install \
                && cd app \
                && yarn install
    export PATH="$PATH:$HOME/.yarn/bin"
  SHELL

  config.vm.provision :shell, privileged:false, run:"always", inline:<<-SHELL
    jupyter notebook --notebook-dir=/vagrant/var/notebook \
                     --no-browser \
                     --ip=0.0.0.0 &
  SHELL

end
