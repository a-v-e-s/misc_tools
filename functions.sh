#!/bin/bash


function sleep_after {

  if [[ -z "$1" ]]; then 
    echo "empty argument!"
    return 1
  fi

  while [[ -n `pidof "$1"` ]]; do
    sleep 10
  done

  sleep 10

  if [[ -n `pidof "$1"` ]]; then
    sleep_after "$1"
  else
    systemctl suspend
  fi
}


function dir_linecount {
  if [[ -z $1 ]]; then
    ext='.py'
  else
    ext="$1"
  fi
  find . -type f -name *"$ext" -exec wc -l {} > /tmp/linecount_$$.txt \;
  cat /tmp/linecount_$$.txt | cut -d ' ' -f1 > /tmp/linecount2_$$.txt
  linecount=`paste -sd+ /tmp/linecount2_$$.txt | bc`
  rm -f /tmp/{linecount,linecount2}_$$.txt
  echo -e "linecount for $ext files in `pwd`:\t$linecount"
}


function cdl {
  cd "$1" && ls
}


function checkfile5 {
  USAGE="checkfile <filepath> <md5_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `md5sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}


function checkfile1 {
  USAGE="checkfile <filepath> <sha1_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `sha1sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}


function checkfile224 {
  USAGE="checkfile <filepath> <sha224_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `sha224sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}


function checkfile256 {
  USAGE="checkfile <filepath> <sha256_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `sha256sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}


function checkfile384 {
  USAGE="checkfile <filepath> <sha384_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `sha384sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}


function checkfile512 {
  USAGE="checkfile <filepath> <sha512_checksum>"
  if ! [[ -f "$1" ]]; then
    echo "$USAGE"
    return 2
  fi
  if [[ `sha512sum "$1" | cut -d ' ' -f1` = "$2" ]]; then
    echo GOOD
    return 0
  else
    echo BAD
    return 1
  fi
}

