#!/bin/bash

declare -a commands
cd ~

index=0
mismatch=false
for i in `ls scripts/`; do
    j=`file "scripts/$i" | grep Repos | sort | cut -d " " -f6 | sed -e 's/Repos/Mutual\/Repos/'`
    k=`file "scripts/$i" | grep Repos | sort | cut -d " " -f1 | sed -e 's/://'`
    if [[ -n "$j" ]] && [[ -n "$k" ]]; then
        commands["$index"]="rm --interactive=never scripts/$i; ln -Ts $j $k;"
        let "index++"
    elif [[ -n "$j" ]] || [[ -n "$k" ]]; then
        echo "Mismatch between $j and $k"
        mismatch=true
        continue
    else
        continue
    fi
done

if ! $mismatch; then
    #echo ${commands[*]}
    for (( a = 0; a < ${#commands[@]}; a++ )); do
        eval ${commands[$a]}
    done
else
    echo "Mismatch between links"
    echo "Matched commands:"
    echo ${commands[*]}
    exit 8
fi