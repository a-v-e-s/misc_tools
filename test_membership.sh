#!/bin/bash

local search="$1"
shift
local list=("$@")
for item in "${list[@]}"; do
    [[ "$item" == "$search" ]] && return 0
done

return 1