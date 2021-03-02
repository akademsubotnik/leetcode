#!/bin/bash

if [ "$#" -ne 2 ]
then
  echo "Not enough arguments"
  break
 elif [ $1 -gt $2 ]
 then
  echo "X is greater"
 elif [ $1 -lt $2 ]
 then
  echo "Y is greater"
 else
  echo "X = Y"
 fi
