#!/bin/bash

#read x and y values in
read x
read y

#perform comparison
if [[ $x -gt $y ]]
then
  echo "X is greater than Y"
elif [[ $x -lt $y ]]
then
  echo "X is less than Y"
else
  echo "X is equal to Y"
fi
