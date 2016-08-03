FROM alpy:0.1
ADD requirements.txt /home/app/
ADD app/ /home/app/
WORKDIR /home/app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "home.py" ]
