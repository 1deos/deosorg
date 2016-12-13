MAINTAINER "atd@bitcoin.sh"

RUN "sudo apt-get install -y nginx $BOOT_DEBUG"

RUN "rm /etc/nginx/nginx.conf"
cat <<EOF>> /deos/var/docker/nginx/nginx.conf
user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
    worker_connections 768;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    gzip on;
    gzip_disable "msie6";
    upstream ipython_server {
      server localhost:8888;
    }
    server {
        listen 80;
        server_name localhost;
        location / {
          proxy_pass http://ipython_server/;
          proxy_http_version 1.1;
          proxy_set_header Upgrade \$http_upgrade;
          proxy_set_header Connection "upgrade";
        }
    }
}
EOF

RUN "ln -s /deos/var/docker/nginx/nginx.conf /etc/nginx/nginx.conf"

RUN "sudo systemctl reload nginx"

RUN "sudo systemctl enable nginx"

EXIT_SUCCESS
