MAINTAINER "atd@bitcoin.sh"
RUN "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -"
echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN "apt-get update"
RUN "apt-get -y install yarn 2> /dev/null"
export PATH="$PATH:`yarn global bin`"
RUN "cd /deos && yarn install && cd app/freebird && yarn install"
EXIT_SUCCESS
