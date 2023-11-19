FROM mcr.microsoft.com/cbl-mariner/base/python:3

RUN yum update -y

WORKDIR /app

COPY ./scripts /app/stress/scripts

WORKDIR /app/stress/scripts
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN pip3 install -r dev_requirement.txt
