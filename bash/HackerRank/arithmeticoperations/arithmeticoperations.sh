#!/bin/bash

#numberone contains the entire expression
#echo "numberone ", $numberone

#declare -i numberone
read numberone

#Will replace spaces with C
#echo $numberone | tr " " "C" | tr "\t" "&"

#Will replace spaces with nothing
#echo $numberone | awk '{ gsub(/ /,""); print }'
#echo $(($numberone)) | bc -l

echo 'scale=3;' $numberone | bc
