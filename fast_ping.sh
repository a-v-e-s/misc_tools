#!/bin/bash
# A very crude script for pinging all ips in a network
# Only works for those with subnet masks of 255.255.255.0

for ip in $1{0..255} ;
do
	(
		ping $ip -c 2 &> /dev/null ;

		if [ $? -eq 0 ];
		then
			echo $ip is alive
		fi
	)&
done
wait
