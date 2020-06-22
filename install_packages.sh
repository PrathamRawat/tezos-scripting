#!/bin/zsh

# Opam installation
sh <(curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh)

# Install rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Use rustup to install rust
rustup toolchain install 1.39.0
rustup default 1.39.0
source $HOME/.cargo/env