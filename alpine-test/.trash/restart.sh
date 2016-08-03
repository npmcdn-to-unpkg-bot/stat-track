#!/usr/bin/env bash

version="$@"

docker stop foo && docker rm foo
docker stop bar && docker rm bar
docker build -t tfight:$version ./ui/
docker build -t tfapi:$version ./api/
docker run -it --name bar -d -p 0.0.0.0:32700:5000 tfapi:$version
docker run -it --name foo -d -p 0.0.0.0:32600:5000 \
	--link bar:bar tfight:$version
docker rmi $(docker images | grep "^<none>" | awk '{print $3}')
docker ps
