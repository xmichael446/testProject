FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y postgresql gcc musl-dev

RUN pip install --upgrade pip setuptools
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .