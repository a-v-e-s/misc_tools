function swap {
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