#[noblacklist]
noblacklist ${HOME}/.weechat

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-secret.inc

#[config]
caps.drop all
seccomp
protocol unix,inet,inet6
netfilter
noroot
