#!/bin/bash

# Update package list and upgrade existing packages
sudo apt-get update
sudo apt-get upgrade -y

#configure unattended updates
sudo apt install unattended-upgrades apt-listchanges -y
sudo dpkg-reconfigure -plow unattended-upgrades

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
sudo apt install nodejs -y

# Install Python 3.12
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install -y python3.12 python3-pip

# Install MariaDB
sudo apt install mariadb-server -y

# Install Nginx
sudo apt install nginx -y

# Enable firewall
sudo ufw allow 22
sudo ufw allow 443
sudo ufw allow 5000
sudo ufw allow 5173
sudo ufw enable

#Création des services
#Front-end
sudo systemctl --force --full edit front-end.service <<EOF
[Unit]
Description=Front end
After=network.target

[Service]
WorkingDirectory=/root/prod_project/ProjetApplicationH2024/front-end/projet_application
ExecStart=/usr/bin/npm run dev -- --host
User=root

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable front-end

#Back-end
sudo systemctl --force --full edit front-end.service <<EOF
[Unit]
Description=My Flask API service
After=network.target

[Install]
WantedBy=multi-user.target
[Service]
Type=simple
User=root
PermissionsStartOnly=true
WorkingDirectory=/root/prod_project/ProjetApplicationH2024/back-end/API
ExecStart=gunicorn -b 0.0.0.0:5000 app:create_app()
Restart=on-failure
TimeoutSec=600
EOF

sudo systemctl enable back-end
