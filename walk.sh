#!/bin/bash

USAGE="./walk.sh [ --dotfiles ] <directory_to_walk>"
MAX_ARGS=2

if [[ $# -gt "$MAX_ARGS" ]]
then
    echo "$USAGE"
    exit 10
fi

while [[ -n $1 ]]
do
    case "$1" in
        --dotfiles)
            DOTFILES=true
            ;;
        *)
            if [[ -d "$1" ]]
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

    if [[ -z "$DOTFILES" ]]
    then
        command="ls"
    else
        command="ls -a"
    fi

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
        while read line
        do
            files[$file_count]="$line"
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