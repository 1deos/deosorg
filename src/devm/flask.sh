DERUN "touch /deos/var/docker/python/app.py"

DERUN "touch /deos/var/docker/python/requirements.txt"

DERUN "touch /deos/var/docker/python/Dockerfile"

DERUN "touch /deos/var/docker/python/docker-compose.yml"

cat << EOF >> /deos/var/docker/python/app.py
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
EOF

cat << EOF >> /deos/var/docker/python/requirements.txt
flask
redis
EOF

cat << EOF >> /deos/var/docker/python/Dockerfile
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
EOF

cat << EOF >> /deos/var/docker/python/docker-compose.yml
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
EOF

DERUN "cd /deos/var/docker/python && docker-compose build"

DERUN "cd /deos/var/docker/python && docker-compose up -d"

EXIT_SUCCESS
