DERUN "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -"

echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

DERUN "apt-get update"

DERUN "apt-get -y install yarn 2> /dev/null"

export PATH="$PATH:`yarn global bin`"

DERUN "cd /deos && yarn install && cd app && yarn install"

EXIT_SUCCESS
