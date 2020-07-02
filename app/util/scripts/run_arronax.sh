#!/bin/bash

docker run -p "$2:80" -e CHAIN_PLATFORM="tezos" -e CHAIN_NETWORK="$3" -e CONSEIL_URL="localhost:$4" -e NODE_URL="localhost:$5" --name "arronax-$1" --network="host" arronax