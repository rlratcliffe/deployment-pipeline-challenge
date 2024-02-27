FROM python:3.11-alpine

LABEL org.opencontainers.image.description API for Dashboard

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1s

WORKDIR /usr/src/app/flask_api
COPY . /usr/src/app/flask_api/
RUN pip3 install poetry
RUN poetry install
RUN poetry show

EXPOSE 5000