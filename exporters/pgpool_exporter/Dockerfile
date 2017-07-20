FROM ubuntu:14.04

MAINTAINER lei.zhu.1017@gmail.com

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y build-essential \
    python \
    python-dev\
    python-pip \
    libpq-dev \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

RUN mkdir -p /opt/pg_conf && mkdir -p /opt/pg_app
COPY ./pgpool_exporter.py /opt/pg_app/
COPY ./pg.json /opt/pg_conf/
