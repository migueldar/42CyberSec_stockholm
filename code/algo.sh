#!/bin/bash

for file in $(find $HOME/infection -type f)
do
	for ex in $(cat /code/extensions)
	do
		if [[ "$file" =~ ^"$ex" ]]
		then
			echo $ex
		fi
	done
done

# for ex in $(cat /code/extensions)
# do
# 	for file in $(find $HOME/infection -type f -name *$ex)
# 	do
# 		echo $ex #call py
# 	done
# done

# EXT_FILE="/code/extensions"

# for file in $(find /root/infection -type f); do
#     for ext_file in $(cat $EXT_FILE); do
#         if [[ $file =~ /root/infection/*$ext_file ]]; then
#             echo $file ' found'
#         fi
#     done
# done