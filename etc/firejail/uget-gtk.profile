#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc

#[config]
caps.drop all
seccomp
protocol unix,inet,inet6
netfilter
noroot

#[whitelist]
whitelist ${DOWNLOADS}
whitelist ~/.config/uGet

#[common]
include /etc/firejail/whitelist-common.inc
