#!/bin/bash


docker rmi $(docker images | grep "^<none>" | awk '{print $3}')

docker-compose down
docker-compose build
docker-compose up -d
docker ps -a


