#!/bin/bash

a=0
while ((a < 10))
do
	# Print the values
	echo $a
	
	# Increment the value
	a=`expr $a + 1`
done
