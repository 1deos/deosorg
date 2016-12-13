#!/usr/bin/env bash

RUN() {
  printf "\x1b[34;01mΔ => [ $1 ]\x1b[34;01m\n"
  echo "$1" | bash
}

ADD_REPO() {
  RUN "add-apt-repository $1"
}

INSTALL() {
  RUN "apt-get -y install $1 $DeOS_BOOT_DEBUG"
}

MAINTAINER() {
  echo "$1" > /dev/null
}

PIP_INSTALL() {
  RUN "pip install $1"
}

PIP_UPGRADE() {
  RUN "pip install --upgrade $1"
}

UPDATE() {
  RUN "apt-get update"
}

UPGRADE() {
  RUN "apt-get -y upgrade $DeOS_BOOT_DEBUG"
}

UPGRADE_PIP() {
  PIP_UPGRADE "pip"
}

EXIT_SUCCESS() {
  exit 0
}

for op in RUN ADD_REPO INSTALL MAINTAINER PIP_INSTALL PIP_UPGRADE UPDATE \
          UPGRADE UPGRADE_PIP EXIT_SUCCESS; do
  export -f $op
done

EXEC() {
  chmod +x "$DeOS_BOOT_PATH/$1.sh"
  exec "$DeOS_BOOT_PATH/$1.sh"
}

while getopts abcnuyvxpdzfjr x; do
  case "$x" in
    a) EXEC "bootstrap" ;;
    b) EXEC "bitcoin" ;;
    c) EXEC "python" ;;
    d) EXEC "blockstack" ;;
    n) EXEC "node" ;;
    u) EXEC "nvm" ;;
    y) EXEC "yarn" ;;
    x) EXEC "nginx" ;;
    r) EXEC "virtualenv" ;;
    m) EXEC "dvm" ;;
    w) EXEC "docker" ;;
    v) EXEC "zerotier" ;;
    z) EXEC "compose" ;;
    f) EXEC "flask" ;;
    j) EXEC "jupyter" ;;
    ?) EXIT_SUCCESS ;;
  esac
done
