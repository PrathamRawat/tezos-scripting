#!/bin/bash

echo $(pwd)

cd util/tezos

./tezos-node config reset

./tezos-node config init --data-dir ../tezos-nodes/tezos-"$1" --network "$1"

./tezos-node config update --data-dir ../tezos-nodes/tezos-"$1" --network "$1" --cors-header='content-type' --cors-origin='*'

./tezos-node identity generate --data-dir ../tezos-nodes/tezos-"$1"

screen -dm -S "tezos-node" ./tezos-node run --data-dir ../tezos-nodes/tezos-"$1" --network "$1" --rpc-addr 127.0.0.1

