#!/bin/bash

# i haven't figured out how to access a literal asterisk from an array
BAD_CHARS=( not_an_asterisk \\ / :  \" \< \> \| ) 
# so I do it from a loop:
for (( a = 0; a < "${#BAD_CHARS[@]}"; a++ )); do
    if [[ "$a" -eq 0 ]]; then
        echo "*"
    else
        echo "${BAD_CHARS["$a"]}";
    fi
done