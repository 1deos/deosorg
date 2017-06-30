include .env-common
ifeq ($(OS_TYPE), Darwin)
	include .env-macos
	include make-macos.mk
endif
ifeq ($(OS_TYPE), Linux)
	include .env-linux
	include make-linux.mk
endif
#[endfi]
