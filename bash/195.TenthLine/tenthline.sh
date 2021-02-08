#!/bin/bash

#Given a text file file.txt, print just the 10th line of the file.

filename='company.txt'
n=1
while read line; do
# reading each line
if [ $n -eq 10 ]
then 
	echo "$line"
fi	
n=$((n+1))
done < $filename









