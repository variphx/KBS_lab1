FROM gcc:latest
WORKDIR /app
RUN apt update

RUN apt-get install git
RUN git config --global init.defaultBranch main

RUN apt-get install make

COPY . .
