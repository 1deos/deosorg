#[noblacklist]
noblacklist ${HOME}/.steam
noblacklist ${HOME}/.local/share/steam

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc

#[config]
caps.drop all
netfilter
noroot
seccomp
protocol unix,inet,inet6
