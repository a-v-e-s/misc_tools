#!/bin/bash
# i have to run this to start docker on my unit:

if [ $EUID != 0 ]; then
	echo "This must be run as root!"
	exit 1
fi

ip link add name docker0 type bridge
ip addr add dev docker0 172.17.0.1/16
