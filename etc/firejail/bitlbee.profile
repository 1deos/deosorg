#[noblacklist]
noblacklist /sbin
noblacklist /usr/sbin

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-common.inc

#[config]
protocol unix,inet,inet6
private
private-dev
seccomp
