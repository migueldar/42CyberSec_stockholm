#!/bin/bash

for file in $(find $HOME/infection -type f)
do
	if [[ "$file" =~ ".ft"$ ]]
	then
		python3 decrypt.py $file $1 $2
	fi
done
