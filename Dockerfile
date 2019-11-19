FROM ubuntu
FROM python

RUN apt-get update
RUN apt-get install build-essential

RUN pip install -U pip
RUN pip install --upgrade pip setuptools
RUN pip install pyrebase

COPY ./app /usr/local/app
COPY java8.tar.gz /usr/local/java8.tar.gz
WORKDIR /usr/local/
CMD ["tar -xf java8.tar.gz"]
WORKDIR /usr/local/app

CMD ["python","script.py"]
ENTRYPOINT bash
