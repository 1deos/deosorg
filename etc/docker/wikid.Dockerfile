FROM ubuntu:14.04
RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential && \
    apt-get install -y libffi-dev libssl-dev && \
    apt-get install -y clang-3.5 llvm && \
    sudo ln -s /usr/bin/clang-3.5 /usr/bin/clang && \
    sudo ln -s /usr/bin/clang++-3.5 /usr/bin/clang++ && \
    apt-get install -y software-properties-common && \
    apt-get install -y curl wget && \
    apt-get install -y byobu git htop man unzip vim && \
    apt-get install -y python-pip python2.7-dev && \
    pip install --upgrade pip && \
    pip install --upgrade virtualenv && \
    pip install pyopenssl ndg-httpsclient pyasn1 && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /wikid
CMD make
