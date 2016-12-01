#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "sudo apt-get install -y ipython"

printd "sudo apt-get install -y ipython-notebook"

printd "sudo pip install jupyter"

printd "sudo pip install ipyparallel"

printd "sudo ipcluster nbextension enable"

printd "sudo ipython profile create vagrant"

if [ -L /root/.ipython/profile_vagrant/ipython_kernel_config.py ]; then
  printd "sudo rm /root/.ipython/profile_vagrant/ipython_kernel_config.py"
fi

cat <<EOT >> /root/.ipython/profile_vagrant/ipython_kernel_config.py
c = get_config()
c.StoreMagics.autorestore = True
c.InteractiveShell.editor = 'vim'
c.AliasManager.user_aliases = [
    ('git', 'git'),
    ('vi', 'vim'),
    ('screen', 'screen'),
    ('make', 'make'),
    ('pip', 'pip'),
    ('node', 'node'),
    ('npm', 'npm'),
    ('yarn', 'yarn'),
]
EOT

sudo jupyter notebook --notebook-dir=/vagrant/var/notebook --no-browser --ip=0.0.0.0 &

exit 0
