docker build -t $1 .
if [ $(uname) = "Darwin" ]; then
	docker run --name $2 -it -v $PWD/code:/code -v $PWD/infection:/root/infection $1
elif [ $(uname) = "Linux" ]; then
	docker run --name $2 -it -v $PWD/code:/code -v $PWD/infection:/root/infection --add-host host.docker.internal:host-gateway $1
fi