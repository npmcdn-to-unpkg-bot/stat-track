# Twitter fight docker container

This file will explain how I built the twitter fight docker container image.

## Starting with the alpine image

I decided to use alpine because it is small. It does not have bash and I happen to like bash so I put bash in the alpine image and called it twitterfight:0.1. I also like vim so I put vim on it.

## Architecture

I will have two containers linked together.

- RethinkDB
- My app

My app will be based on the alpine linux container. It will house the flask-api and the flask-ui.Unfortunately I will not build a container with an easy one-line ```docker run [...]``` instruction.

...

## Python

I've added python to the Dockerfile and the name is now tfight:0.2. In addition to python I added a Flask app and it works. I give a one-line ```docker run``` command and the Flask app runs a web page on localhost.

## My minimal Jenkins

Every change I make I had to manually restart everything. So I created a bash script that does that automatically. It is 5 lines of code.

My next step is to add some D3.

## Version 0.2.2.2

I have a simple flask app that renders data driven elements using d3. And I got this all done before noon. What a boss.

## The API container

I've started building the API container. It is also based on alpine 3.4 and flask. My app will consist of three containers:
- The database (rethinkdb)
- The ui (flask on alpine linux)
- The api (flask on alpine linux)

For now I'm going to build an api without a library. Basically I'm reinventing the wheel but with an API that talks to rethinkdb.

## 12 hours later

I've built a very basic api. The UI flask app and the API flask app are linked via the docker --link flag. I've also added some d3 code. The dummy data supplied by my API is being rendered in d3 by the UI flask app. The resulting page looks very simple. Very simple indeed, but it is very functional. The flexibility provided by the container architecture is superb and it is the best in the world. So far this is the structure I have.
```
.
├── api
│   ├── app
│   │   ├── static
│   │   ├── templates
│   │   ├── conn.py
│   │   └── home.py
│   ├── Dockerfile
│   └── restart.sh
├── ui
│   ├── app
│   │   ├── static
│   │   │   ├── css
│   │   │   ├── d3
│   │   │   │   ├── API.md
│   │   │   │   ├── CHANGES.md
│   │   │   │   ├── d3.js
│   │   │   │   ├── d3.min.js
│   │   │   │   ├── LICENSE
│   │   │   │   └── README.md
│   │   │   └── js
│   │   │       └── data.js
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   └── home.html
│   │   └── hello.py
│   ├── Dockerfile
│   └── restart.sh
├── notes.md
└── restart.sh

11 directories, 18 files
```

My minimal Jenkins has evolved into the restart.sh script in the root directory. It essentially rebuilds the two containers that make up my app right now. It also removes <none> images and allows me to enter easy versioning numbers. I've built up to version 0.3.3.

I have no tests.
