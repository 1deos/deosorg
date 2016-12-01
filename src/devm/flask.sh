#!/usr/bin/env bash

printd() {
    printf "\x1b[34;01m########[ $1 ]########\x1b[34;01m\n";
    echo "$1" | bash;
}

printd "touch /vagrant/var/docker/python/app.py"

printd "touch /vagrant/var/docker/python/requirements.txt"

printd "touch /vagrant/var/docker/python/Dockerfile"

printd "touch /vagrant/var/docker/python/docker-compose.yml"

cat <<EOT >> /vagrant/var/docker/python/app.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
EOT

cat <<EOT >> /vagrant/var/docker/python/requirements.txt
flask
redis
EOT

cat <<EOT >> /vagrant/var/docker/python/Dockerfile
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
EOT

cat <<EOT >> /vagrant/var/docker/python/docker-compose.yml
version: '2'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
    depends_on:
     - redis
  redis:
    image: redis
EOT

printd "cd /vagrant/var/docker/python && docker-compose build"

printd "cd /vagrant/var/docker/python && docker-compose up -d"

exit 0
