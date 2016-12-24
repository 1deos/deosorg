#!/bin/sh

HOST_OS=$(uname)

EXIT_SUCCESS() {
  exit 0
}

EXIT_FAILURE() {
  exit 1
}

deos_bin() {
  for path in .deos/bin/darwin .deos/bin/vagrant .deos/bin/travis
  do
    [ ! -f "$path/tao" ] && cp src/tao.py $path/tao
    [ -f "$path/tao" ] && chmod +x $path/tao
    [ ! -f "$path/logger" ] && cp src/logger.py $path/logger
    [ -f "$path/logger" ] && chmod +x $path/logger
    [ ! -f "$path/print" ] && cp src/print.py $path/print
    [ -f "$path/print" ] && chmod +x $path/print
    [ ! -f "$path/spinner" ] && cp src/spinner.sh $path/spinner
    [ -f "$path/spinner" ] && chmod +x $path/spinner
  done
}

deos_venv() {
  path=.deos/venv/$1
  bin=virtualenv
  venv=default
  flag=--no-site-packages
  [ ! -d "$path/$venv" ] && (cd $path && $bin $venv $flag)
}

deos_init() {
  [ ! -d ".cache" ] && mkdir .cache
  for path in .deos .deos/bin .deos/obj .deos/venv\
              .deos/bin/darwin .deos/bin/vagrant .deos/bin/travis\
              .deos/obj/darwin .deos/obj/vagrant .deos/obj/travis\
              .deos/venv/darwin .deos/venv/vagrant .deos/venv/travis
  do
    [ ! -d "$path" ] && mkdir $path
  done
}

deos_clean() {
  [ -d ".vagrant" ] && rm -rf .vagrant/
  [ -d ".deos" ] && rm -rf .deos/
  [ -d "src/web" ] && rm -rf src/web/
  [ -d "doc/web" ] && rm -rf doc/web/
  [ -d "test/web" ] && rm -rf test/web/
  [ -f "boot/init.lz" ] && rm boot/init.lz
  [ -f "boot/python.lz" ] && rm boot/python.lz
  [ -f "src/example.sh" ] && rm src/example.sh
  [ -f ".editorconfig" ] && rm .editorconfig
  [ -f ".gitignore" ] && rm .gitignore
  [ -f ".nvmrc" ] && rm .nvmrc
  [ -f ".travis.yml" ] && rm .travis.yml
  [ -f "bootstrap.test.sh" ] && rm bootstrap.test.sh
  [ -f "Makefile" ] && rm Makefile
}

deos_darwin() {
  deos_clean
  deos_init
  deos_venv "darwin"
  deos_bin
  .deos/bin/darwin/tao
  EXIT_SUCCESS
}

deos() {
  case "${HOST_OS:-nil}" in
    Darwin)
      deos_darwin
    ;;
    Linux)
      EXIT_FAILURE
    ;;
    *)
      EXIT_FAILURE
    ;;
  esac
}

main() {
  deos
}

main
