function swap {
    if [ "${1:1}" -eq 0 ]
    then
        echo True
        return 0
    fi
    
    b=`echo "${1:1}""${1:0:1}"`
    if [ $1 -ge $b ]
    then
        echo True
        return 0
    else
        echo False
        return 1
    fi
}

function date_difference {
    echo "Enter Date 1 in the format yyyy-mm-dd :"
    read date1
    echo "Enter Date 2 in the format yyyy-mm-dd :"
    read date2
    difference=$(( `date -d "$date1" +%s` / 86400 - `date -d "$date2" +%s` / 86400 ))
    echo $difference
    return $difference
}