#!/bin/bash

for a in 1 2 3 4 5 6 7 8 9 10
do
	# if a is equal to 9 break the loop
	if [ $a == 9 ]
	then
		break
	fi
	
	# Print the value
	echo "Iteration no $a"
done
