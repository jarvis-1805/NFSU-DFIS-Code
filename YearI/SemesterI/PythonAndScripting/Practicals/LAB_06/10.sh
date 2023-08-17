#!/bin/bash

myarray=("cat" "dog" "mouse" "frog")
echo 'index start from zero for accessing'
echo 'use curly braces to access index'
echo ${myarray[@]}
echo ${myarray[1]}
echo ${myarray[@]}
myarray+=("mango" "banana")
echo ${myarray[@]}
myarray[2]=grapes
echo ${myarray[@]}
unset myarray[2]
echo ${myarray[@]}
