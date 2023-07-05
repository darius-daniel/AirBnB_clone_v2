#!/usr/bin/bash
# A script that sets up web servers for the deployment of web_static
apt update -y
apt install -y nginx

if [ ! -d /data/web_static/releases ]
then
  mkdir -p /data/web_static/releases/test/
fi

if [ ! -d /data/web_static/shared ]
then
  mkdir -p /data/web_static/shared/
fi

echo "Hello World!" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]
then
  rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

service nginx restart
