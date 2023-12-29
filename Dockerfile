FROM node:18-alpine3.19
COPY python-app .
RUN apt-get update && apt-get install -y curl
EXPOSE 8080
CMD [ "/bin/ls", "-l" ]
ENTRYPOINT [ "/opt/app/run.sh", "--port", "8080" ] 