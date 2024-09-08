#!/usr/bin/env bash
set -euo pipefail

sudo apt install python3-pip python3-rpi.gpio python3-w1thermsensor python3-dotenv

python setup.py
python main.py

# add python main.py to cron
