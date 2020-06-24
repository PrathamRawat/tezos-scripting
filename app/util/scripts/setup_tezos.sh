#!/bin/bash

cd util

# Delete old tezos repository
if [ -d "tezos" ]; then
  echo "Removing Tezos"
  rm -rf tezos
  echo "Removed"
fi

# Clone repository and initialize opam
git clone https://gitlab.com/tezos/tezos.git
cd tezos
git checkout latest-release
opam init --bare -a

# Create compiler version for ocaml
opam switch create tezos 4.09.1
eval $(opam env)

# Get binaries
opam install depext
opam depext tezos

# Install binaries
opam install tezos -y