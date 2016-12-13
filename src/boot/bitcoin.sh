MAINTAINER "atd@bitcoin.sh"
ADD_REPO "ppa:bitcoin/bitcoin" && UPDATE
INSTALL "bitcoind"
RUN "bitcoin-cli"
EXIT_SUCCESS
