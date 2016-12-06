DERUN "apt-get update"

DERUN "apt-get -y upgrade 2> /dev/null"

DERUN "apt-get -y install build-essential 2> /dev/null"

DERUN "apt-get -y install llvm 2> /dev/null"

DERUN "apt-get -y install clang 2> /dev/null"

DERUN "apt-get -y install libssl-dev 2> /dev/null"

DERUN "apt-get -y install git 2> /dev/null"

DERUN "apt-get -y install curl 2> /dev/null"

DERUN "apt-get -y install apt-transport-https"

DERUN "apt-get -y install ca-certificates"

EXIT_SUCCESS
