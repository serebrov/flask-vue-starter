#!/bin/bash
set -e

if [ ! -d "/src/venv" ]; then
  cd /src
  virtualenv -p python3 venv
  # See the note below.
  # virtualenv --relocatable venv
fi

source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
# Note: this doesn't acutally work, it tries to rewrite paths in venv
# to make them relative, but it doesn't change the absolute path in
# the venv/bin/activate, so venv still can not be used.
# So for now - venv is available on the host, but only works inside
# docker container.
# virtualenv --relocatable venv

exec "$@"
