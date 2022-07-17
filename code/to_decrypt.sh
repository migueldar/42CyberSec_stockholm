#!/bin/bash

for file in $(find $HOME/infection -type f -name *.ft)
do
	python3 decrypt.py $file $1 $2
done
