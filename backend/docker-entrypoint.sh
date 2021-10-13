#!/bin/bash
set -e

if [ ! -d "/src/venv" ]; then
  # Create new virtual environment
  python3 -m venv /src/venv
else
  # Activate existing virtual environment
  source /src/venv/bin/activate
fi

# Always refresh dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

exec "$@"
