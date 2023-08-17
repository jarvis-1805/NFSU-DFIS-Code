#!/bin/bash

myArray=("cat" "dog" "mouse" "frog")
echo 'Not ! Only to access index ${!myArray[@]}'
for i in ${!myArray[@]}
do
	echo "Element $i is ${myArray[$i]}"
done
