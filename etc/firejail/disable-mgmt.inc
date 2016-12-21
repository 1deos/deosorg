#[sys:dirs]
blacklist /sbin
blacklist /usr/sbin
blacklist /usr/local/sbin

#[sys:mgmt]
blacklist ${PATH}/umount
blacklist ${PATH}/mount
blacklist ${PATH}/fusermount
blacklist ${PATH}/su
blacklist ${PATH}/sudo
blacklist ${PATH}/xinput
blacklist ${PATH}/evtest
blacklist ${PATH}/xev
blacklist ${PATH}/strace
blacklist ${PATH}/nc
blacklist ${PATH}/ncat
