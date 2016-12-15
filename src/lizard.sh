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

NEW() {
  RUN "touch $1"
}

PIP_INSTALL() {
  RUN "pip install $1"
}

PIP_UPGRADE() {
  RUN "pip install --upgrade $1"
}

RM() {
  RUN "rm -rf $1"
}

UPDATE() {
  RUN "apt-get update"
}

UPGRADE() {
  RUN "$DeOS_CMD_APT_UPGRADE"
}

UPGRADE_PIP() {
  PIP_UPGRADE "pip"
}

SUDO_SYSD_ENABLE() {
  RUN "sudo systemctl enable $1"
}

SUDO_SYSD_RELOAD() {
  RUN "sudo systemctl reload $1"
}

SUDO_INSTALL() {
  RUN "sudo apt-get -y install $1 $DeOS_BOOT_DEBUG"
}

EXIT_SUCCESS() {
  exit 0
}

EXIT_FAILURE() {
  exit 1
}

for op in RUN ADD_REPO INSTALL MAINTAINER NEW PIP_INSTALL PIP_UPGRADE RM\
          UPDATE UPGRADE UPGRADE_PIP SUDO_INSTALL SUDO_SYSD_RELOAD\
          SUDO_SYSD_ENABLE EXIT_FAILURE EXIT_SUCCESS; do
  export -f $op
done

EXEC() {
  chmod +x "$DeOS_BOOT_PATH/$1.lz"
  exec "$DeOS_BOOT_PATH/$1.lz"
}

PRINT() {
  printf "\x1b[34;01mP => [ $1 ]\x1b[34;01m\n"
}

while getopts "a:bcdefnuyvxpzijr" OPT; do
  case "$OPT" in
    a) PRINT $OPTARG && EXEC "bootstrap" ;;
    b) EXEC "bitcoind" ;;
    c) EXEC "python" ;;
    d) EXEC "blockstack" ;;
    e) EXEC "nginx" ;;
    f) EXEC "docker" ;;
    n) EXEC "node" ;;
    u) EXEC "nvm" ;;
    y) EXEC "yarn" ;;
    r) EXEC "virtualenv" ;;
    m) EXEC "dvm" ;;
    v) EXEC "zerotier" ;;
    z) EXEC "compose" ;;
    i) EXEC "flask" ;;
    j) EXEC "jupyter" ;;
    ?) EXIT_SUCCESS ;;
  esac
done
