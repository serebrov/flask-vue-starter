FROM python:3.12-slim-bookworm

ARG UID
ARG GID

# The -o option permits to add a group with a non-unique GID.
# It fixes the "groupadd: GID '20' already exists" error on Mac.
RUN groupadd -o -g $GID user
RUN useradd -m -u $UID -g user user
USER user

WORKDIR /backend
