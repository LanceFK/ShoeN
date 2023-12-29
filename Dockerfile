FROM baseImage:tag
COPY hello.txt /absolute/path
RUN apt-get update && apt-get install -y curl
EXPOSE 8080
CMD [ "/bin/ls", "-l" ]
ENTRYPOINT [ "/opt/app/run.sh", "--port", "8080" ] 