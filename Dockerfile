FROM node:18-alpine3.19
COPY . /src/venv
RUN cd /src/venv
EXPOSE 5432
CMD [ "C:/Program Files/Git/bin/bash.exe", "--login", "-i" ]
ENTRYPOINT [ "shoe1in", "--port", "5432"] 