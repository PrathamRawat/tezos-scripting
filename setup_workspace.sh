#!/bin/bash

#DEPENDENCIES FOR NODE

sudo apt-get install curl

sudo apt-get install python3

sudo apt-get install python3-pip

sudo apt-get install screen

pip3 install flask

pip3 install psutil

cd app

./util/scripts/install_packages.sh

./util/scripts/setup_tezos.sh

./util/scripts/build_tezos.sh

sudo apt-get install git

sudo apt-get install docker.io

sudo groupadd docker

sudo usermod -aG docker $USER

# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
sudo apt-get install postgresql

sudo pg_ctlcluster 12 main start

# Create postgres user for current account
sudo -u postgres createuser -s $(whoami);
