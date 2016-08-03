#!/usr/bin/env bash

version="$@"

docker stop bar && docker rm bar
docker build -t tfapi:$version .
docker run -it --name bar -d -p 0.0.0.0:32700:5000 tfapi:$version
docker ps
