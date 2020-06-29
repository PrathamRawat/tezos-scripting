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

cd util

sudo apt-get install git

git clone https://github.com/Cryptonomic/Conseil.git

sudo apt-get install docker.io

sudo groupadd docker

sudo usermod -aG docker $USER

sudo apt-get install postgres