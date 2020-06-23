#!/bin/bash

cd ..

cd tezos

if [ "$1" == "-d" ]; then
    echo "Building Developer Mode"
    make build-dev-deps
else
    make build-deps
fi

eval $(opam env)

make
