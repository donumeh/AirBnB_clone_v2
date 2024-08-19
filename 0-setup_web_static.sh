#!/usr/bin/env bash
# Sets up a web server for deployement of web_static

# Install Nginx if not already installed
sudo apt-get update && sudo apt-get install nginx -y

# Create some new folders along a path if they don't already exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared/

# Create a fake HTML file in */test
echo "<h1>Hello HBNB</h1>" \
	| sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link and delete old ones
sudo rm -f /data/web_static/current

# Create the link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the `ubuntu` user
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Start Nginx service
sudo service nginx start


