#!/bin/bash
# mgrep.sh is like grep for manpages
# At least I hope it will be soon.

usage="Usage: mgrep.sh [-o] <search_string>"

open=0
while getopts ":o:" x; do
    case $x in
        o) open=1;;
        *) echo $usage; exit 1;;
    esac
done
shift $((OPTIND-1))

man_path=`manpath | tr ":" " "`

for i in $man_path; do
    ls -LR $i 2>/dev/null | col >> /tmp/man_files.$$
done

index=0
declare -a results
while read line; do
    name=`echo $line | tr -d ":"` # wtf is the problem with this line?
    if [[ -d $name ]]; then
        dir=$name
    elif [[ -n `echo "$name" | grep "$1"` ]]; then
        fullpath=$dir/$name
        results[$index]=$fullpath
        let index++
    fi
done < /tmp/man_files.$$

if [[ open -eq 1 && ${#results[@]} -eq 1 ]]; then
    man ${results[0]}
elif [[ ${#results[@]} -gt 0 ]]; then
    echo "Matching Files:"
    for i in $results; do
        echo $i
    done
else
    echo "No Matches Found."
fi