FROM azurecr.io/shoe1in:49e6f29c7f6c1e3e234693284d1a2d34e71d9a22
WORKDIR /app
ADD . /app
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt