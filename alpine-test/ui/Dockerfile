FROM alpy:0.1
ADD app/ /home/app/
ADD requirements.txt /home/app/
WORKDIR /home/app

RUN apk add curl && \
    pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "/home/app/hello.py" ]

