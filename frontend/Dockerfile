FROM node:20-alpine

# Install shadow package for usermod/groupmod commands
RUN apk add --no-cache shadow

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

# Change ownership of the workdir to node user
RUN chown -R node:node /frontend

# Switch to node user
USER node

# Copy package files first (for better Docker layer caching)
COPY --chown=node:node package*.json ./

# Install dependencies inside the container (for correct architecture)
RUN npm ci

# Copy source code
COPY --chown=node:node . .

# Expose Vite dev server port
EXPOSE 5173

# Start Vite development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]