FROM node:18-alpine3.19
COPY . /src
RUN cd /src
EXPOSE 8080
CMD [ "/bin/ls", "-l" ]
ENTRYPOINT [ "/opt/app/run.sh", "--port", "8080" ] 