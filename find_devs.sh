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

git log > /tmp/$$.log
awk '/Author:/ { print $2, $NF } ' /tmp/$$.log | tr -d '<>' | sort | uniq | tee /tmp/$$.authors
awk '/Author:/ { print $2, $NF, prev; name=$2; email=$NF } ' /tmp/$$.log | tr -d '<>' | sort | uniq | tee /tmp/$$.authors
awk '/Date:/ { print $6, name, email; name=$2; email=$NF } ' /tmp/$$.log | tr -d '<>' | sort | uniq | tee /tmp/$$.authors
grep -n -m 1 $line /tmp/$$.log

for field in `awk '/Author:/ { print $NF }' test.txt`; do
  echo -e "$field:\t`grep -c $field test.txt`" >> /tmp/$$.count
done

sort /tmp/$$.count | uniq | sort -k2 -nr

# goes from (email: count) to (printing date of last commit)
count=0
for field in `cat fjdslkanfdsa`; do
  let count++
  if [ $(( $count % 2 )) -eq 0 ]; then
    name="$field"
    echo -e "$name\t$date\t$email" >> output.txt
    continue
  fi
  line=$(( `grep -n -m 1 "${field:0:-1}" /tmp/$$.log | cut -d ':' -f1` + 1 ))
  date=`sed -n "$line p" /tmp/$$.log | cut -d ' ' -f8`
  email="$field"
done


count=0
for line in `cat newest.14491`; do
  let count++
  name=""; email=""; year=""; contribs=""
  if [ $(( $count % 3 )) -eq 1 ]; then
    line2=`grep -m 1 "$line" /tmp/$$.log`
    name=`echo "$line2" | cut -d ' ' -f2`
    email="$line"
  elif [ $(( $count % 3 )) -eq 2 ]; then
    year="$line"
  elif [ $(( $count % 3 )) -eq 0 ]; then
    contribs="$line"

    if [ -n "$name" ] && [ -n "$email" ] && [ -n "$year" ] && [ -n "$contribs" ]; then
      echo -e "\n$name\t$email\t$year\t$contribs\n" >> output2.txt
    fi
  fi
done

while read line; do
  email=`echo "$line" | cut -d ' ' -f1`
  year=`echo "$line" | cut -d ' ' -f2`
  contributions=`echo "$line" | cut -d ' ' -f3`

  line=$(( `grep -n -m 1 "${email}" /tmp/$$.log | cut -d ':' -f1` ))
  name=`sed -n "$line p" /tmp/$$.log | cut -d ' ' -f2,3`

  echo -e "\nname:\t$name\nemail:\t$email\nlast contribution:\t$year\ncontributions:\t$contributions" >> $$.output
done < <( cat emails.txt )



rm /tmp/$$*