FROM node:18-alpine3.19
COPY . /src/venv/bin/activate
RUN cd /src/venv/bin/activate
EXPOSE 5432
ENTRYPOINT [ "sh", "bash" ]