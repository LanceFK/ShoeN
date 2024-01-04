FROM node:18-alpine3.19
COPY . /src
RUN cd /src
EXPOSE 8080
CMD [ "/bin/ls", "-l" ]
ENTRYPOINT [ "/bin/bash", "--port", "8080" ] 