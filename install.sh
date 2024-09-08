#!/usr/bin/env bash
sudo apt install python3-pip python3-rpi.gpio python3-w1thermsensor

pip install python-dotenv

python setup.py
python main.py

# add python main.py to cron
