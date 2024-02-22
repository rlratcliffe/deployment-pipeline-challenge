FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip3 install poetry
RUN poetry install

EXPOSE 8000