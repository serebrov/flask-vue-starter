FROM node:16.11

# Install global NPM dependencies in non-root user directory
# https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#global-npm-dependencies
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

# Set user 'node' to have same UID and GID as current user on host
# https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#non-root-user
ARG GID
ARG UID

# The -o option permits to add a group with a non-unique GID.
# It fixes the "groupadd: GID '20' already exists" error on Mac.
RUN groupmod -o -g $GID node && usermod -u $UID -g $GID node

WORKDIR /frontend
