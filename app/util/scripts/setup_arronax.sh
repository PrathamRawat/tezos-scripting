#!/bin/bash

cd util

git clone https://github.com/Cryptonomic/Arronax.git

cd Arronax

git checkout dockerfile-develeop

docker build -t arronax .

