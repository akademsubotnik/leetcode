#!/bin/bash

#read first value to get total number of passed numbers
read numbers
echo $numbers

START=1
SUM=0

for (( c=$START; c<=$numbers; c++ ))
do
  read value
  #SUM = $SUM + $
  #num=$(($num1 + $num2))
  SUM=$(($SUM + $value))
done

echo $(($SUM / 100))
