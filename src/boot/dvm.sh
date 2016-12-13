MAINTAINER "atd@bitcoin.sh"
RUN "curl -sL $DVM_INSTALL | sh"
source $DVM_ACTIVATE && dvm install
echo "source $DVM_ACTIVATE" >> $VM_BASHRC
echo "export DOCKER_VERSION=$DOCKER_VERSION" >> $VM_BASHRC
echo "dvm use" >> $VM_BASHRC
EXIT_SUCCESS
