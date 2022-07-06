# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"

# install system dependencies
RUN apt-get update \
  && pip install --upgrade pip \
  && apt-get clean


# install python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .
