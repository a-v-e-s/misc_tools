#!/bin/bash

# ctime.sh modified from an obscure StackOverflow Q&A
# prints the creation date of any number of files passed to it
# only known to work on ext4 filesystems


for fn in "${@}"; do
    # get inode of every argument
    inode=$(stat -c %i "${fn}")
    # find its partition
    fs=`df  --output=source "${fn}"  | tail -1`
    hextime=$(
        # use debugfs to get a load of information on the file
        # and chop it up to find the creation time:
        sudo debugfs -R 'stat <'"${inode}"'>' "${fs}" 2>/dev/null | 
        grep crtime: |
        egrep -o '[0-9a-f]{8}'|
        head -1 | 
        tr 'a-f' 'A-F'
    )
    # turn into decimal, print seconds since unix epoch:
    crtime=`echo "ibase=16; $hextime" | bc`
    echo $crtime
done