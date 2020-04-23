#!/bin/bash

# This script gets all the scripts found anywhere
# within a directory or any of its subdirectories
# and creates symbolic links to them in 
# a single, convenient directory.
#
# It also adds execute permissions for user and group
# if they are not already present.
#
# It is useful if you have a directory with multiple repositories
# which have multiple scripts within multiple subdirectories,
# etc.

USAGE="Usage: $ `basename $0` <scripts_directory> <directory_for_links>"
scripts="$1"
links="$2"

# Make sure the user has used the correct syntax:
if [[ ! -d "$scripts" || ! -d "$links"  || $# != 2 ]]; then
	echo "$USAGE"
	exit 1
fi

# Make sure we are working with absolute directory paths:
if [[ ${scripts:0:1} != "/" ]]; then
	scripts=`realpath "$scripts"`
fi
if [[ ${links:0:1} != "/" ]]; then
	links=`realpath "$links"`
fi

# Get all directories, subdirectories, and all of their files:
ls -R "$scripts" | col > /tmp/linker.$$

# Combine the directory names with their filenames,
# then test to see if it contains a "shebang"
# to determine if it is a script,
# and create a link in the $links directory if so:
while read line; do
	case "$line" in 
		"")
			continue
			;;
		/*:)	# catches all of the directories
			dir="${line:0:${#line}-1}"
			;;
		*)		# catches all files within previous directory
			fn="$dir"/"$line"
			if [[ -d "$fn" ]]; then
				continue
			elif [[ `head -n 1 "$fn"` =~ ^#! ]]; then
				# Make sure the file is executable
				if [[ ! -x "$fn" ]]; then
					chmod ug+x "$fn"
				fi
				link_name=`basename "$fn" | cut -d "." -f1`
				ln -Ts "$fn" "$links"/"$link_name"
			fi
			;;
	esac
# Bash likes to tell you about all the null bytes it ignores
# in command substitution, which is not helpful so
# we send those warnings into a black hole here:
done < /tmp/linker.$$ 2>/dev/null

echo -e "\nDone!\n"

exit 0
