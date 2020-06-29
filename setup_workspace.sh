#!/bin/bash

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

