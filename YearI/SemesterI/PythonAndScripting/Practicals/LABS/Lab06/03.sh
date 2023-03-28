#!/bin/bash

echo "hi"
read -p "Enter a number 1 or 2 or 3: " i

if (($i == 1))
then
	echo 'i is equal to one.'
elif (($i == 2))
then
	echo 'i is equal to two.'
elif (($i == 3))
then
	echo 'i is equal to three.'
else
	echo 'It is neither one nor two nor three.'
fi
