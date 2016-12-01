#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -"

printd "sudo apt-get -y install nodejs 2> /dev/null"

printd "sudo apt-get -y install npm 2> /dev/null"

exit 0
