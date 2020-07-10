#!/bin/bash

cd util

mkdir tezos-nodes

cd tezos-nodes

mkdir data

cd data

mkdir "$4"

cd "$4"

if [ "$1" == "mainnet" ]; then
    if [ "$5" == "full" -o "$5" == "archive" ]; then
        wget https://snaps.tulip.tools/mainnet_2020-07-10_12:21.full -O img
    fi
    if [ "$5" == "experimental-rolling" ]; then
        wget https://snaps.tulip.tools/mainnet_2020-07-10_12:21.rolling -O img
    fi
else
    if [ "$5" == "full" -o "$5" == "archive" ]; then
        wget https://snaps.tulip.tools/carthagenet_2020-07-10_12:21.full -O img
    fi
    if [ "$5" == "experimental-rolling" ]; then
        wget https://snaps.tulip.tools/carthagenet_2020-07-10_12:21.rolling -O img
    fi
fi

docker run --rm -v "$PWD/:/var/run/tezos/node" -v "$PWD/img:/snapshot" "tezos/tezos:$1" tezos-snapshot-import

docker run -d -v "$PWD/:/var/run/tezos/node" --network="host" --name "tezos-node-$4" "tezos/tezos:$1" tezos-node --cors-header='content-type' --cors-origin='*' --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3" --history-mode "$5"

rm img