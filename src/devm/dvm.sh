DERUN "curl -sL https://download.getcarina.com/dvm/latest/install.sh | sh"

source /home/vagrant/.dvm/dvm.sh

export DOCKER_VERSION=1.8.2

dvm install

echo "source /home/vagrant/.dvm/dvm.sh" >> /home/vagrant/.bashrc

echo "export DOCKER_VERSION=1.8.2" >> /home/vagrant/.bashrc

echo "dvm use" >> /home/vagrant/.bashrc

EXIT_SUCCESS
