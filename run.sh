#!/bin/bash

prompt=$1
shift
urls=("$@")

python3 ./main.py --prompt "\"$prompt\"" --url "$urls"