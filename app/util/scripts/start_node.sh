#!/bin/bash

cd tezos

./tezos-node config reset

./tezos-node config init

./tezos-node identity generate

./tezos-node run
