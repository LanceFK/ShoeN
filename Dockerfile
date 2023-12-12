FROM alpine:3.10

RUN pip install -r requirements.txt 

COPY . .

ADD requirements.txt /code/

WORKDIR /app
# ENTRYPOINT ["/entrypoint.sh"]

CMD [ "executable" ]
