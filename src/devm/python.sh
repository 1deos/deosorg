#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "sudo apt-get install -y python2.7"

printd "sudo apt-get install -y python-dev"

printd "sudo apt-get install -y python-pip"

printd "sudo pip install --upgrade pip"

printd "sudo pip install ndg-httpsclient"

printd "sudo pip install pyasn1"

printd "sudo pip install --upgrade requests[security]"

exit 0
