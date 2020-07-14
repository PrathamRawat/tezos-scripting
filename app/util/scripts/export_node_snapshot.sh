#!/bin/bash

cd "util/tezos-nodes/data/$1"

mkdir snapshots

docker run --rm -v "$PWD/snapshots:/snapshots/file.full" -v "$PWD:/var/run/tezos" --entrypoint ./$BIN_DIR/tezos-node "tezos/tezos-bare:latest-release" snapshot export /snapshots/file.full