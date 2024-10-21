FROM python:latest
WORKDIR /app
RUN apt update

RUN apt-get install git
RUN git config --global init.defaultBranch main

COPY . .
