# Notes about ambassador containers

## Commands
```
$ docker-machine create -d virtualbox redis-host
$ docker-machine create -d virtualbox identidock-host

$ eval $(docker-machine env redis-host)
$ docker run -d --name real-redis redis:3
...

$ docker run -d --name real-redis-ambassador \
    -p 6379:6379 \
    --link real-redis:real-redis \
    amouat/ambassador
...

$ eval $(docker-machine env identidock-host)
$ docker run -d --name redis_ambassador
    --expose 6379 \
    -e REDIS_PORT_6379_TCP=tcp://$(docker-machine ip redis-host):6379 \
    amouat/ambassador
...

$ docker run -d --name dnmonster amouat/dnmonster:1.0
...

$ docker run -d --link dnmonster:dnmonster \
    --link redis_ambassador:redis \
    -p 80:9090 \
    amouat/identidock:1.0
```
