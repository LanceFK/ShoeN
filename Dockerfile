FROM acrshoen.azurecr.io/shoe1in:alpine

RUN pip install -r requirements.txt 

COPY . .

ADD requirements.txt /code/

WORKDIR /app

CMD [ "executable" ]
