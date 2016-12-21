#[noblacklist]
noblacklist ${HOME}/.gnupg

#[include]
include /etc/firejail/disable-mgmt.inc
include /etc/firejail/disable-secret.inc
include /etc/firejail/disable-devel.inc

#[blacklist]
#include /etc/firejail/disable-common.inc thunderbird icedove
blacklist ${HOME}/.adobe
blacklist ${HOME}/.macromedia
blacklist ${HOME}/.filezilla
blacklist ${HOME}/.config/filezilla
blacklist ${HOME}/.purple
blacklist ${HOME}/.config/psi+
blacklist ${HOME}/.remmina
blacklist ${HOME}/.tconn

#[config]
caps.drop all
seccomp
protocol unix,inet,inet6
netfilter
tracelog
noroot
