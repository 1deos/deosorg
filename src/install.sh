#!/bin/sh

make clean
rm -rf .deos/

mkdir .deos
mkdir .deos/bin
mkdir .deos/bin/darwin
mkdir .deos/bin/linux
mkdir .deos/etc
mkdir .deos/etc/darwin
mkdir .deos/etc/darwin/python
mkdir .deos/etc/linux
mkdir .deos/etc/linux/python
mkdir .deos/etc/linux/nginx
mkdir .deos/ext
mkdir .deos/ext/darwin
mkdir .deos/ext/linux
mkdir .deos/obj
mkdir .deos/obj/darwin
mkdir .deos/obj/linux
mkdir .deos/venv
mkdir .deos/venv/darwin
mkdir .deos/venv/linux

touch .deos/etc/linux/python/requirements.txt
cat <<EOF>> .deos/etc/linux/python/requirements.txt
web.py==0.38
EOF

touch .deos/etc/linux/python/requirements.blockstack.txt
cat <<EOF>> .deos/etc/linux/python/requirements.blockstack.txt
base58==0.2.4
basicrpc==0.0.2
bitcoin==1.1.42
bitmerchant==0.1.8
blockstack==0.14.0.7
blockstack-profiles==0.14.0
blockstack-zones==0.14.0
boto==2.43.0
cachetools==2.0.0
cffi==1.9.1
commontools==0.1.0
cryptography==1.6
defusedxml==0.4.1
ecdsa==0.13
enum34==1.1.6
functools32==3.2.3.post2
idna==2.1
ipaddress==1.0.17
jsonschema==2.5.1
jsontokens==0.0.2
keychain==0.1.4.1
keylib==0.0.5
mixpanel==4.3.1
protocoin==0.2
pyasn1==0.1.9
pybitcoin==0.9.9
pycparser==2.17
pycrypto==2.6.1
python-bitcoinrpc==0.1
requests==2.12.3
simplejson==3.10.0
six==1.10.0
utilitybelt==0.2.6
virtualchain==0.14.0
EOF

cp src/spinner.sh .deos/bin/darwin/spinner
chmod +x .deos/bin/darwin/spinner

cp src/deos.py .deos/bin/darwin/deos
chmod +x .deos/bin/darwin/deos

cp src/print.py .deos/bin/darwin/printm
chmod +x .deos/bin/darwin/printm

rm -rf var/build/
mkdir var/build

make x=blockstack venv

bash -c "\
source .deos/venv/darwin/blockstack/bin/activate\
&& pip install blockstack"

.deos/bin/darwin/deos
#make yubikey
