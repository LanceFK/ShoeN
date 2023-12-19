FROM node:18-alpine3.19
COPY . /src
RUN cd /src
EXPOSE 5432
CMD ["node", "/src/server.js"]