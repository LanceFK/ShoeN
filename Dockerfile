FROM node:15-alpine
COPY . /src
RUN cd /src
EXPOSE 80
CMD ["node", "/src/server.js"]