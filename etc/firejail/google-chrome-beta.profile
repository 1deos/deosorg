#[noblacklist]
noblacklist ${HOME}/.config/google-chrome-beta

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
#include /etc/firejail/disable-devel.inc

#[config]
netfilter

#[whitelist]
whitelist ${DOWNLOADS}
whitelist ~/.config/google-chrome-beta
whitelist ~/.cache/google-chrome-beta

#[common]
include /etc/firejail/whitelist-common.inc
