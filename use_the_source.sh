# A collection of bash aliases and functions I find useful:
#
# Usage:
# `$ source path/to/use_the_source.sh`
# `$ <sourced command> [arguments]` 
# Or:
# `$ cat path/to/use_the_source.sh >> ~/.bashrc`
#


# aliases:
alias shutdown='sudo shutdown -P now'
alias cyberghost='sudo openvpn openvpn.ovpn | tee logs/`date +%j-%H-%M`.log'
alias fucking='sudo'
alias open='xdg-open'
alias mv='mv -i'
alias cp='cp -i'
alias rm='rm -i'
alias jupyter='python3 -m jupyterlab'
alias mkdir='mkdir -p'
alias shred='shred -uz'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'
alias .......='cd ../../../../../..'
alias ........='cd ../../../../../../..'
alias .........='cd ../../../../../../../..'
alias ..........='cd ../../../../../../../../..'
alias ...........='cd ../../../../../../../../../..'


function disk_destroyer {
    # Make sure the user sent us a block device:
    if [[ `file "$1" | cut -d ' ' -f2` != "block" ]]
    then
        echo "$1 is not a block device!"
        exit 2
    fi
    #
    # Confirm the user really wants us to erase this device:
    echo -en "Really overwrite $1 ?\nThis cannot be undone!\nConfirm [y/n]: "
    read reply
    if [[ "$reply" != "y" ]]
    then
        echo "Reply was $reply instead of \"y\". Exiting now..."
        exit 3
    fi
    #
    # Write disk with ones, then zeroes, then random data,
    # then tell user we are done:
    sudo cat /dev/zero | tr '\000' '\377' > "$1"
    sudo dd bs=1M if=/dev/zero of="$1"
    sudo dd bs=1M if=/dev/urandom of="$1"
    echo DONE!
}


function startup {
    xdg-open ~/Documents/personal/{budget,functionality}.ods
    firejail brave-browser
}