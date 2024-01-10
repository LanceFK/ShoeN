FROM node:18-alpine3.19
COPY . /src/venv
RUN cd /src/venv
EXPOSE 8080
ENTRYPOINT [ "/ShoeN_App/newProj", "shoe1in" ] 