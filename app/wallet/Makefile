export MAKEFLAGS=--no-print-directory

all: venv sip pyqt

brew:
	-brew install protobuf
	-brew install pyqt5
	-brew install sip

venv:
	-rm -rf .venv
	-virtualenv --always-copy --no-site-packages .venv

sip:
	-rm -rf ext/sip
	cp .cache/sip-4.18.1.tar.gz sip.tar.gz
	gunzip sip.tar.gz
	tar -xvf sip.tar
	rm -rf sip.tar
	mv sip-4.18.1 ext/sip
	source .venv/bin/activate && \
	cd ext/sip && \
	python configure.py --incdir=../../.venv/include/python2.7 && \
	make && \
	make install

pyqt:
	-rm -rf ext/pyqt
	cp .cache/PyQt-mac-gpl-4.11.4.tar.gz pyqt.tar.gz
	gunzip pyqt.tar.gz
	tar -xvf pyqt.tar
	rm -rf pyqt.tar
	mv PyQt-mac-gpl-4.11.4 ext/pyqt
	source .venv/bin/activate && \
	cd ext/pyqt && \
	python configure-ng.py --qmake=/usr/local/Cellar/qt5/5.7.0/bin/qmake && \
	make && \
	make install
