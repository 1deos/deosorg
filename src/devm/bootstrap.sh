#!/usr/bin/env bash

DERUN() {
  printf "\x1b[34;01mΔ => [ $1 ]\x1b[34;01m\n"
  echo "$1" | bash
}

EXIT_SUCCESS() {
  exit 0
}

export -f DERUN
export -f EXIT_SUCCESS

while getopts cnuyvxpdbzfj x
do
  case "$x" in
    c)  (chmod +x "/deos/src/devm/common.sh")
        (exec "/deos/src/devm/common.sh") ;;
    n)  (chmod +x "/deos/src/devm/node.sh")
        (exec "/deos/src/devm/node.sh") ;;
    u)  (chmod +x "/deos/src/devm/nvm.sh")
        (exec "/deos/src/devm/nvm.sh") ;;
    y)  (chmod +x "/deos/src/devm/yarn.sh")
        (exec "/deos/src/devm/yarn.sh") ;;
    x)  (chmod +x "/deos/src/devm/nginx.sh")
        (exec "/deos/src/devm/nginx.sh") ;;
    p)  (chmod +x "/deos/src/devm/python.sh")
        (exec "/deos/src/devm/python.sh") ;;
    b)  (chmod +x "/deos/src/devm/dvm.sh")
        (exec "/deos/src/devm/dvm.sh") ;;
    d)  (chmod +x "/deos/src/devm/docker.sh")
        (exec "/deos/src/devm/docker.sh") ;;
    v)  (chmod +x "/deos/src/devm/zerotier.sh")
        (exec "/deos/src/devm/zerotier.sh") ;;
    z)  (chmod +x "/deos/src/devm/compose.sh")
        (exec "/deos/src/devm/compose.sh") ;;
    f)  (chmod +x "/deos/src/devm/flask.sh")
        (exec "/deos/src/devm/flask.sh") ;;
    j)  (chmod +x "/deos/src/devm/jupyter.sh")
        (exec "/deos/src/devm/jupyter.sh") ;;
    ?)  EXIT_SUCCESS ;;
  esac
done
