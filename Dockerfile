FROM acrshoen.azurecr.io/shoe1in:fd03082ad90dcea037c2069014fd0a06e76b885c
COPY . /src
RUN cd /src
EXPOSE 5432
CMD ["node", "/src/server.js"]