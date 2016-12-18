#!/bin/sh

spinner() {
  while true; do
    printf '△\b' && sleep 0.1
    printf '▷\b' && sleep 0.1
    printf '▽\b' && sleep 0.1
    printf '◁\b' && sleep 0.1
  done
}

main() {
  printf "\033[30;1m$1\033[0m\n"
  spinner &
  spinner_pid=$!
  printf '\e[?25l'
  $1
  printf '\e[?25h'
  kill $spinner_pid
  wait $spinner_pid 2> /dev/null
  printf ' '
  printf '\n'
}

main "$1"
