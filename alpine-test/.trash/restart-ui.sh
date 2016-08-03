#!/usr/bin/env bash

version="$@"

docker stop foo && docker rm foo
docker build -t tfight:$version .
docker run -it --name foo -d -p 0.0.0.0:32600:5000 \
	--link bar:bar tfight:$version
docker ps
