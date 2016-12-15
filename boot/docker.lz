MAINTAINER "atd@bitcoin.sh"
sudo apt-key adv --keyserver $DOCKER_KEY_SERV --recv-keys $DOCKER_GPG_KEY
sudo apt-key adv --keyserver $UBUNTU_KEY_SERV --recv-keys $UBUNTU_GPG_KEY
echo "deb $DOCKER_APT_REPO $DOCKER_UBUNTU main" | sudo tee $DOCKER_SOURCES
RUN "sudo apt-get update"
RUN "sudo apt-get -y install linux-image-extra-$(uname -r)"
RUN "sudo apt-get -y install linux-image-extra-virtual $BOOT_DEBUG"
RUN "sudo apt-get -y install docker-engine $BOOT_DEBUG"
RUN "sudo service docker start"
RUN "sudo usermod -aG docker vagrant"
RUN "sudo systemctl enable docker"
EXIT_SUCCESS
