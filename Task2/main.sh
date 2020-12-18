#!/usr/bin/bash

help_message="Script name : $0 \n\
Description : call the 4 scripts from Task 1 and the checker script to check on the input and the output of each script\n\
Usage : main.sh <directory_ws > <top_module> <prefix> [remove_comment] \n\
Arguments : \n\
<arg 1> : your path \n\
<arg 2> : top_module \n\
<arg 3> : prefix ITI_ or DIC_ \n\
<arg 4> : write remove_comment to check comment is removed \n\
Example :main.sh task_ws top ITI_ remove_comment \n\
$0 arg1 arg2 "

if [ $1 == "-h" ] 
then
	echo -e $help_message
	exit
fi
./checker.py c1 $1
	if [ $? == 0 ] 
	then
		echo c1
		exit
	fi
./update_dir.py $1

./checker.py c1-1 $1
	if [ $? == 0 ] 
	then
		echo c1-1
		exit
	fi
./checker.py c2 $3 $4
	if [ $? == 0 ] 
	then
		echo c2
		exit
	fi
./add_prefix.py $1 $3 $4

./checker.py c2-1 $1 $2 $3 $4 
	if [ $? == 0 ] 
	then
		echo c2-1
		exit
	fi
./create_tree.py $1

./checker.py c3 $1
	if [ $? == 0 ]
	then
		echo c3
		exit
	fi
./create_rpt.py $1
