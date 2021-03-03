#!/bin/bash

read sideone
read sidetwo
read sidethree

#EQUILATERAL
if [ $sideone -eq $sidetwo ] && [ $sidetwo -eq $sidethree ]
then
  echo "EQUILATERAL"
#SCALENE
elif [ $sideone -ne $sidetwo ] && [ $sideone -ne $sidethree ] && [ -$sidetwo -ne $sidethree ]
then
  echo "SCALENE"
else
  echo "ISOSCELES"
fi
