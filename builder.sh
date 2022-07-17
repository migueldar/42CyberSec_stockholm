docker build -t $1 .
docker run --name $2 -it -v $(PWD)/code:/code -v $(PWD)/infection:/root/infection $1