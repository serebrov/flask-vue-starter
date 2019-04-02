#!/bin/bash
set -e

if [ ! -d "/src/venv" ]; then
  cd /src
  virtualenv -p python3 venv
  virtualenv --relocatable venv
fi

source venv/bin/activate
pip install -q -r requirements.txt
pip install -q -r requirements-dev.txt
virtualenv --relocatable venv

exec "$@"
