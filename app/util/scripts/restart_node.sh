#!/bin/bash

cd util/tezos

screen -dm -S "$4" ./tezos-node run --data-dir ../tezos-nodes/data/"$4" --config-file ../tezos-nodes/config/"$4".json --network "$1" --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3"
