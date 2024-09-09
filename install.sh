#!/usr/bin/env bash
set -euo pipefail

sudo apt install python3-pip

python -m venv venv
source ./venv/bin/activate

pip3 install -r requirements.txt

python setup.py
python main.py

# add python main.py to cron
