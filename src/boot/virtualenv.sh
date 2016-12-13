MAINTAINER "atd@bitcoin.sh"
RUN "pip install virtualenv"
RUN "cd /deos/venv/linux/ && virtualenv python --no-site-packages"
RUN "source /deos/venv/linux/python/bin/activate && pip install -r /deos/requirements.txt"
cat << EOF >> /deos/venv/linux/python/.gitignore
#[ignore]
*

#[except]
!.gitignore
EOF
EXIT_SUCCESS
