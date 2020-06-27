#!/bin/bash

declare -a PAGES
PAGES+=('https://store.pine64.org/product/pinephone-community-edition-ubports-limited-edition-linux-smartphone/')
PAGES+=('https://store.pine64.org/product/pinetab-10-1-linux-tablet-with-detached-backlit-keyboard/')
PAGES+=('https://store.pine64.org/product/pinetab-10-1-linux-tablet/')

index=0
for page in "${PAGES[@]}"; do
	wget -q -O /tmp/$$.$index "${PAGES[$index]}"
	echo "${PAGES[$index]:33:-1}"
	if [[ -n `cat /tmp/$$.$index | egrep '[Oo]ut [Oo]f [Ss]tock'` ]]; then
		cat /tmp/$$.$index | egrep '[Oo]ut [Oo]f [Ss]tock'
	else
		echo "Probably in stock"
	fi 

	rm /tmp/$$.$index
	let index+=1
done
