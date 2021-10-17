#!/bin/bash
set -e

if [ ! -d "/backend/venv" ]; then
  # Create new virtual environment
  python3 -m venv /backend/venv
else
  # Activate existing virtual environment
  source /backend/venv/bin/activate
fi

# Always refresh dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

exec "$@"
