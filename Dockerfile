FROM alpine:3.10

# RUN pip install -r requirements.txt 

COPY entrypoint.sh /entrypoint.sh

# ADD requirements.txt /code/

# WORKDIR /app
ENTRYPOINT ["/entrypoint.sh"]

CMD [ "executable" ]
