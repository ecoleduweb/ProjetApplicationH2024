#!/bin/bash

# Update package list and upgrade existing packages
sudo apt-get update
sudo apt-get upgrade -y

#configure unattended updates
sudo apt install unattended-upgrades apt-listchanges -y
sudo dpkg-reconfigure -plow unattended-upgrades

# Install Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
sudo apt install nodejs -y

source ~/.nvm/nvm.sh

nvm install v20.11.0

# Install Python 3.12
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install -y python3.12

# Install MariaDB
sudo apt install mariadb-server -y

# Enable firewall
sudo ufw allow 22
sudo ufw allow 443
sudo ufw allow 5000
sudo ufw enable

sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
