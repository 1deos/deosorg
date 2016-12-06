DERUN "apt-get install -y python2.7 2> /dev/null"

DERUN "apt-get install -y python-dev 2> /dev/null"

DERUN "apt-get install -y python-pip 2> /dev/null"

DERUN "pip install --upgrade pip"

DERUN "pip install ndg-httpsclient"

DERUN "pip install pyasn1"

DERUN "pip install --upgrade requests[security]"

EXIT_SUCCESS
