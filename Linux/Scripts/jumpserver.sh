#!/bin/bash

info_department() {
cat department | while read line
do
    echo ${line}
done
}

info_server_soft5() {
cat soft5-server | while read line
do
    echo ${line}
done
}

info_public_server() {
cat public_server | while read line
do
    echo ${line}
done
}

ssh_server_ip(){
	server_ip=$(awk "NR==$server" soft5-server | awk '{print $2}' )
	echo "contecting to ${server_ip} ..."
	ssh root@${server_ip}
}


clear


while :
do
	info_department
	read -p "please choice department number: " cho

	case $cho in
	1)
		info_server_soft5
		read -p "please choice server number: " server
		ssh_server_ip
		break
	;;
	2)
		info_public_server
		read -p "please choice server number: " server
        	ssh_server_ip
		break
	;;
	3)
        	echo 3
	;;
	q)
        	exit
	;;
	h)
        	clear
	        echo "Enter as follows the correct options"
	;;
	*)
        	clear
	        echo "please enter Correct Options"
	;;
	esac
done
