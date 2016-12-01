#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

git clone https://github.com/creationix/nvm.git /home/vagrant/.nvm && cd /home/vagrant/.nvm && git checkout `git describe --abbrev=0 --tags`

source /home/vagrant/.nvm/nvm.sh

cd /vagrant && nvm install && nvm use

n=$(which node); n=${n%/bin/node}; chmod -R 755 $n/bin/*; sudo cp -r $n/{bin,lib,share} /usr/local

exit 0
