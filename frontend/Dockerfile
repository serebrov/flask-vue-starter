FROM node:8.15

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

RUN npm install -g npm@latest; \
    npm install -g @vue/cli;

WORKDIR /src

# Restore npm packages
COPY package.json yarn.lock ./

RUN yarn install

COPY . .
