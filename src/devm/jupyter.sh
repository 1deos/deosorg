DERUN "apt-get install -y ipython"
DERUN "apt-get install -y ipython-notebook 2> /dev/null"
DERUN "pip install jupyter"
DERUN "pip install ipyparallel"
DERUN "ipcluster nbextension enable"
DERUN "ipython profile create deos"

if [ -L /root/.ipython/profile_deos/ipython_kernel_config.py ]; then
  DERUN "rm /root/.ipython/profile_deos/ipython_kernel_config.py"
fi

cat << EOT >> /root/.ipython/profile_deos/ipython_kernel_config.py
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

sudo jupyter notebook --notebook-dir=/deos/var/notebook \
                      --no-browser --ip=0.0.0.0 &

EXIT_SUCCESS
