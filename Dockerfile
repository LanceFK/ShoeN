FROM node:18-alpine3.19
COPY . /src/venv/bin/activate
RUN cd /src/venv/bin/activate
EXPOSE 8080
# CMD [ "/bin/ls", "-l" ]
ENTRYPOINT [ "/ShoeN_App/newProj", "shoe1in" ] 