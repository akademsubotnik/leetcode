#!/bin/bash

read sideone
read sidetwo
read sidethree

#EQUILATERAL
if [ $sideone -eq $sidetwo ] && [ $sidetwo -eq $sidethree ]
then
  echo "EQUILATERAL"
#ISOSCELES
elif [ $sideone -eq $sidetwo ] || [ $sideone -eq $sidethree ] || [ $sidetwo -eq $sidethree ]
then
  echo "ISOSCELES"
#SCALENE
else
  echo "SCALENE"
fi
