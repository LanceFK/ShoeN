FROM acrshoen.azurecr.io/shoe1in:latest

RUN pip install -r requirements.txt 

COPY . .

ADD requirements.txt /code/

WORKDIR /app

CMD [ "executable" ]
