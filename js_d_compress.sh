#!/bin/bash
# A very crude tool for compressing and decompressing javascript

Usage="./js_d_compress.sh (-c|-d) input_file output_file"

if [ $1 == "-c" ]; then
	cat $2 | \
	tr -d '\n\t' | \
	tr -s ' ' | \
	sed 's:/\*.*\*/::g' | \
	sed 's/ \?\([{}();,:]\) \?/\1/g' \
	> $3
elif [ $1 == "-d" ]; then
	cat $2 | \
	sed 's/;/;\n/g' | \
	sed 's/{/{\n/g' | \
	sed 's/}/\n}/g' \
	> $3
else
	echo $Usage
fi
