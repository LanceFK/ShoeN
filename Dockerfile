FROM node:18-alpine3.19
COPY . /src/venv/bin/activate
RUN cd /src/venv/bin/activate
EXPOSE 5432
CMD [ "C:/Program Files/Git/bin/bash.exe", "--login", "-i" ]
ENTRYPOINT [ "C:/Users/K Fam/Desktop/ShoeN_App/ShoeN", "shoe1in", "--port", "5432"] 