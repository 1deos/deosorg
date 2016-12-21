#[noblacklist]
noblacklist ${HOME}/.config/google-chrome

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
#include /etc/firejail/disable-devel.inc

#[config]
netfilter

#[whitelist]
whitelist ${DOWNLOADS}
whitelist ~/.config/google-chrome
whitelist ~/.cache/google-chrome

#[common]
include /etc/firejail/whitelist-common.inc
