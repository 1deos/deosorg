#[whitelist]
whitelist ~/.Mathematica
whitelist ~/.Wolfram Research
whitelist ~/Documents/Wolfram Mathematica

#[include]
include /etc/firejail/whitelist-common.inc
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc

#[config]
caps.drop all
seccomp
noroot
