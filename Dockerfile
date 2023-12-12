FROM node:15-alpine
COPY . /src
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["node", "/src/server.js"]