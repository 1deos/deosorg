#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -"

echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

printd "sudo apt-get update && sudo apt-get -y install yarn 2> /dev/null"

export PATH="$PATH:`yarn global bin`"

printd "cd /vagrant && yarn install && cd app && yarn install"

exit 0
