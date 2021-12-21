#!/usr/bin/env bash
# sets the web server for the deployement

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y intall nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Testers" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
