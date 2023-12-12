FROM alpine:3.10

RUN pip install -r requirements.txt 

COPY . .

ADD requirements.txt /code/

WORKDIR /app
# ENTRYPOINT ["/entrypoint.sh"]

CMD [ "executable" ]
FROM ubuntu:latest
WORKDIR /app
ADD . /app
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt