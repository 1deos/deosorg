#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-common.inc
include /etc/firejail/disable-devel.inc

#[whitelist]
whitelist ${HOME}/.local/share/mupen64plus/
whitelist ${HOME}/.config/mupen64plus/

#[config]
noroot
caps.drop all
seccomp
net none
