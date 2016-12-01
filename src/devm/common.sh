#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "sudo apt-get update"

printd "sudo apt-get -y install build-essential 2> /dev/null"

printd "sudo apt-get -y install llvm"

printd "sudo apt-get -y install clang"

printd "sudo apt-get -y install libssl-dev 2> /dev/null"

printd "sudo apt-get -y install git 2> /dev/null"

printd "sudo apt-get -y install curl 2> /dev/null"

exit 0
