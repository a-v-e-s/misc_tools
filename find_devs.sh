#!/bin/bash

# exit with helpful message if first (only) argument is not a directory:
if ! [[ -d "$1" ]]; then
  echo -e "USAGE:\t$ find_devs.sh <path_to_git_repo>"
  exit 1
fi

# change to code repository directory and find all the commit authors:"
pushd "$1"
git log | awk '/Author:/ { print $2, $NF } ' | tr -d '<>' | sort | uniq | tee /tmp/$$.results
popd
echo "Output temporarily saved in /tmp/$$.results"
exit 0