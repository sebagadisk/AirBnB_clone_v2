#!/usr/bin/env bash
<<<<<<< HEAD
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
=======
# sets the web server for the deployement

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y intall nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Testers" | sudo tee /data/web_static/releases/test/index.html
>>>>>>> 8f5a422a0ab8934862d1d6635b6180100cb53a35
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
