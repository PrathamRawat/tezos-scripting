#!/bin/bash

cd util/tezos

./tezos-node config reset

./tezos-node config --data-dir ../tezos-nodes/data/"$4" --network "$1" --config-file ../tezos-nodes/config/"$4".json init

./tezos-node config --data-dir ../tezos-nodes/data/"$4" --network "$1" --config-file ../tezos-nodes/config/"$4".json --cors-header='content-type' --cors-origin='*' --rpc-addr 127.0.0.1:"$2" -listen-addr 127.0.0.1:"$3" update

./tezos-node identity generate --data-dir ../tezos-nodes/data/"$4" --config-file ../tezos-nodes/config/"$4".json

screen -dm -S "$4" ./tezos-node run --data-dir ../tezos-nodes/"$4" --config-file ../tezos-nodes/config/"$4".json --network "$1" --rpc-addr 127.0.0.1:"$2" -listen-addr 127.0.0.1:"$3"

