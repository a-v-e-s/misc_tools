#!/bin/bash

USAGE="./all_dat.sh <directory> <.dat file>"

if [[ ! -d "$1" ]] || [[ ! -f "$2" ]]; then
    echo "$USAGE"
    exit 1
fi

for file in `find "$1" -maxdepth 0 -type f`; do
    checksum=`md5sum "$file" | cut -d ' ' -f1`
    echo "$checksum" >> "$2"
done