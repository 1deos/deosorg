MAINTAINER "atd@bitcoin.sh"
curl -s $ZT_GPG_KEY | gpg --import
curl -s $ZT_INSTALL | gpg --output - >$ZT_INSTALL_TMP && bash $ZT_INSTALL_TMP
sudo zerotier-cli join $ZT_NETWORK
EXIT_SUCCESS
