#[noblacklist]
noblacklist ${HOME}/.config/opera-beta

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc

#[config]
netfilter

#[whitelist]
whitelist ~/.config/opera-beta
whitelist ${DOWNLOADS}
whitelist ~/.cache/opera-beta

#[common]
include /etc/firejail/whitelist-common.inc
