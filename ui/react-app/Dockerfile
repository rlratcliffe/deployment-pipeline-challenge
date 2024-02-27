FROM node:21.6.2-alpine

LABEL org.opencontainers.image.description UI for Dashboard

WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY ./package.json ./
COPY public/ ./public
COPY src/ ./src
RUN npm install --silent

EXPOSE 3000