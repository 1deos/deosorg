#!/bin/sh

#[host]
HOST_OS=$(uname)

#[pass]
EXIT_SUCCESS() {
  exit 0
}

#[fail]
EXIT_FAILURE() {
  exit 1
}

#[endfi]
