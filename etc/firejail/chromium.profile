#[noblacklist]
noblacklist ${HOME}/.config/chromium

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
#include /etc/firejail/disable-devel.inc

#[config]
netfilter
whitelist ${DOWNLOADS}
whitelist ~/.config/chromium
whitelist ~/.cache/chromium

#[common]
include /etc/firejail/whitelist-common.inc
