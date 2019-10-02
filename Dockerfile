FROM frolvlad/alpine-gcc
FROM ubuntu
FROM python

RUN apt-get update
RUN apt install build-essential

RUN pip install -U pip
RUN pip install --upgrade pip setuptools
RUN pip install pyrebase

COPY ./app app

WORKDIR "./app"
