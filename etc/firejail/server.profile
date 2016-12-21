#[noblacklist]
noblacklist /sbin
noblacklist /usr/sbin

#[include]
include /etc/firejail/disable-mgmt.inc

#[private]
private
private-dev
private-tmp

#[config]
seccomp
