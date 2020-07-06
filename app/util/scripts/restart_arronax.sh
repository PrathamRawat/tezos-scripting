#!/bin/bash

docker start -d --network="host" --name "arronax-$1" "arronax-$1"