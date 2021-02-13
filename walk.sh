#!/bin/bash

# It's remarkably slow tbqh...

MAX_ARGS=2
USAGE="./walk.sh [ --dotfiles ] <directory_to_walk>"

if [[ $# -gt "$MAX_ARGS" ]]
then
    echo "$USAGE"
    exit 10
fi

while [[ -n $1 ]]
do
    case "$1" in
        --dotfiles)
            DOTFILES=1
            ;;
        *)
            if [[ -d "$1" ]] && [[ -z "target" ]]
            then
                target="$1"
            else
                echo "$USAGE"
                exit 10
            fi
            ;;
    esac
    shift
done


function step {
    pushd "$1" > /dev/null

    local count=0
    local dir_count=0
    local file_count=0
    declare -a directories files

    [[ -z "$DOTFILES" ]] && command="ls" || command="ls -a"

    for fd in `"$command"`
    do
        if [[ -d "$fd" ]]
        then
            directories[$dir_count]="$fd"
            let dir_count++
        elif [[ -f "$fd" ]]
        then
            files[$file_count]=`pwd`"/$fd"
            let file_count++
        fi
    done
    
    for d in "${directories[@]}"
    do
        while read fn
        do
            files[$file_count]="$fn"
            let file_count++
        done < <(step "$d")

    done

    for f in "${files[@]}"
    do
        echo "$f"
    done

    popd > /dev/null
}


step "$target"

exit 0