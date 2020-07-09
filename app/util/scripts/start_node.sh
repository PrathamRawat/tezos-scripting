#!/bin/bash

cd "../tezos-nodes/"

mkdir "data/$4"

if [ "$1" == "mainnet" ]; then
    docker run -d --network="host" --name "tezos-node-$4" tezos/tezos:mainnet tezos-node --cors-header='content-type' --cors-origin='*' --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3" --history-mode "$5"
else
    docker run -d --network="host" --name "tezos-node-$4" tezos/tezos:master tezos-node --cors-header='content-type' --cors-origin='*' --network "$1" --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3" --history-mode "$5"
fi

#./tezos-node config --config-file ../tezos-nodes/config/"$4".json reset

#./tezos-node config --data-dir ../tezos-nodes/data/"$4" --network "$1" --config-file ../tezos-nodes/config/"$4".json init

#./tezos-node config --data-dir ../tezos-nodes/data/"$4" --network "$1" --config-file ../tezos-nodes/config/"$4".json --cors-header='content-type' --cors-origin='*' --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3" update

#./tezos-node identity --data-dir ../tezos-nodes/data/"$4" --config-file ../tezos-nodes/config/"$4".json generate

#screen -dm -S "$4" ./tezos-node run --data-dir ../tezos-nodes/data/"$4" --config-file ../tezos-nodes/config/"$4".json --network "$1" --rpc-addr 127.0.0.1:"$2" --net-addr 127.0.0.1:"$3" --history-mode "$5"

#export node_pid=$(screen -ls | awk '/\."$4"\t/ {print strtonum($1)}')
