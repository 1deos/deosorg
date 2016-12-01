#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install -y apt-transport-https ca-certificates

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F76221572C52609D

echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get update

apt-cache policy docker-engine

sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual

sudo apt-get install -y docker-engine

sudo service docker start

sudo usermod -aG docker $USER

sudo systemctl enable docker

exit 0
