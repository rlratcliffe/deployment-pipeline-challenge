FROM node:21.6.2-alpine

WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY ./package.json ./
RUN npm install --silent

EXPOSE 3000