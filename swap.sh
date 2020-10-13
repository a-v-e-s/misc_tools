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

function gripper {
    if ! [[ -f $1 ]]
    then
        echo "Must supply log file as first argument"
        exit 1
    fi

    start=$(date --date=`grep "Started at" $1 | awk '{print $6 "-" $4 "-" $5 "-" $7; }' | sed 's/\.//'` +%s)
    end=$(date --date=`grep "Terminated at" $1 | awk '{print $6 "-" $4 "-" $5 "-" $7; }' | sed 's/\.//'` +%s)
    cpu_time=`grep "CPU time" $1 | awk '{print $4}'`
    max_mem=`grep "Max Memory" test.txt | awk '{print $4}'`
    walltime=$(( $end - $start ))
    efficiency=`bc <<< "scale=2; $cpu_time / $walltime"`

    echo "Job started at: `grep "Started at" $1 | awk '{print $4 "-" $5 "-" $7 " " $6 }' | sed 's/\.//'`"
    echo "Job ended at: `grep "Terminated at" test.txt | awk '{print $4 "-" $5 "-" $7 " " $6 }' | sed 's/\.//'`"
    echo "CPU Time: $cpu_time"
    echo "Max Memory used: $max_mem"
    echo "Walltime: $walltime"
    echo "Efficiency (cpu time / wall time): $efficiency"
}