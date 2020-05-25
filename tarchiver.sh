#!/bin/bash

USAGE="\
\n\
Usage: `basename $0` <target-directory> <file-extension> ( [ -a <max-tar-age-in-days> ] || \
[ -s <max-tar-size-in-kb> ] || [ -f <max-number-of-archived-files> ] ) [ -l <layers-of-backup-tarchives> ] \
[ -h || --help ] \n\
\n\
Default max age = 360\n\
Default max size in kb = 10TB\n\
Default max number of compressed backup archive layers=2\n\
There is no limit to the number of file in the tar archive by default.\n\
Usual recommendation is to use only one option of {-a,-s,-f} to limit the archiving,\n\
and to set the -l option to the number of rotated, compressed backups to keep.\n\
tarchiver.sh requires root permission to get dates of files!\n\
\n\
For example:\n\
\n\
$ sudo ./tarchiver.sh ~/Documents/special_documents .ext -a 720        # keep archives up to 720 days old and one compressed layer\n\
$ ./tarchiver.sh ~/Documents/special_documents .ext -s 1000000         # limit size to 1,000,000 KB (1 GB)\n\
$ ./tarchiver.sh ~/Documents/special_documents .ext -f 200             # limit to maximum of 200 files in archive\n\
$ ./tarchiver.sh ~/Documents/special_documents .ext -l 4               # limit layers of compressed tarball backups of tar archives\n\
$ sudo ./tarchiver.sh ~/Documents/special_documents .ext -a 365 -l 4   # limit archive age to 365 days, keep 4 layers of compressed backup archives.\n\
$ ./tarchiver.sh ~/Documents/special_documents .ext -s 1000 -l 4       # rotate if size exceeds 1000 kb, keep 4 layers of compressed backup archives.\n\
$ ./tarchiver.sh ~/Documents/special_documents .ext -f 24 -l 2         # rotate if archive has > 24 files, keep 4 layers of compressed backup archives.\n\
$ ./tarchiver.sh -h                                                    # display this message and exit.\n\
\n\
-a -s and -f options only apply to the uncompressed tar archive.\n\
Note that tarchiver.sh likely will not work for filesystems other than ext4\n\
\n\
"


# function to get the time a file was created, in unix epoch time
# only tested on ext4 filesystem...
get_crtime() {
    for target in "${@}"; do
        inode=$(stat -c %i "${target}")
        fs=`df  --output=source "${target}"  | tail -1`
        hextime=$(
            sudo debugfs -R 'stat <'"${inode}"'>' "${fs}" 2>/dev/null | 
            grep crtime: |
            egrep -o '[0-9a-f]{8}'|
            head -1 | 
            tr 'a-f' 'A-F'
        )
        crtime=`echo "ibase=16; $hextime" | bc`
        printf "%s" $crtime
    done
}


# option parsing logic:
if [[ $# -lt 2 || ! -d "$1" ]]; then
    # not enough arguments or first argument not a directory
    echo -e $USAGE
    exit 1
elif [[ `ls "$1"/*"$2" 2>/dev/null; echo $?` -eq 2 ]]; then
    echo "No files found in $1 with extension $2"
    exit 2
else
    DIR="$1"
    EXT="$2"
    TARCHIVE_NAME="$2".tar
    LAYERS=2
    ROTATE=false
    # parse the remainder of options:
    shift 2
    while [ -n $1 ]; do
        case $1 in
            -a)
                if [[ $(( `get_crtime $TARCHIVE_NAME` / 86400 )) -gt "$2" ]]; then
                    ROTATE=true
                fi
                shift 2
                ;;
            -s)
                if [[ `du $TARCHIVE_NAME | cut -f1` -gt "$2" ]]; then
                    ROTATE=true
                fi
                shift 2
                ;;
            -f)
                if [[ `tar -tvf $TARCHIVE_NAME | wc -l ` -gt "$2" ]]; then
                    ROTATE=true
                fi
                shift 2
                ;;
            -l)
                LAYERS="$2"
                shift 2
                ;;
            *)
                echo -e $USAGE
                exit 1
                ;;
        esac
    done
fi


# if time to rotate, do that first, removing excess archives as necessary
# if time to compress, do that next.
# if time to archive, then do that
cd "$DIR"
if [ $ROTATE ]; then
    # put names of tarballs into a temporary file:
    ls *.tar.gz.[0-9] > $$.temp
    # get the number from the end of each name and put it in another temp file:
    IFS='.'
    while read line; do
        read -ra NUM <<< "$line"
        echo ${NUM[3]} >> $$.temp2
    done < $$.temp
    # rotate the compressed archives:
    for i in `cat $$.temp2 | sort`; do
        if [ $i -lt 9 && $i -lt $LAYERS ]; then
            j=$(( i + 1 ))
            mv $TARCHIVE_NAME.tar.gz.$i $TARCHIVE_NAME.tar.gz.$j
        else
            rm $TARCHIVE_NAME.tar.gz.$i
        fi
    done
    # compress the uncompressed tarchive, create new one in its place:
    tar -zvf $TARCHIVE_NAME.tar
    tar -cvf *.$EXT
else
    # if not rotating archives, just append new files to the archive:
    tar -rvf $TARCHIVE_NAME.tar *.$EXT
fi


# remove temp files:
rm $$.temp $$.temp2