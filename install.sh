#!/usr/bin/env bash
set -euo pipefail

pip3 --version > /dev/null 2>&1 || {
  sudo apt install python3-pip
}

if [ ! -d venv ]
then
  python -m venv venv
fi
source ./venv/bin/activate

pip3 install -r requirements.txt

python setup.py

echo "API token was configured successfully."

grep "dtoverlay=w1-gpio" /boot/firmware/config.txt > /dev/null 2>&1 || {
  echo "dtoverlay=w1-gpio" | sudo tee -a /boot/firmware/config.txt
  echo "Updated /boot/firmware/config.txt. Rebooting now..."
  sudo reboot now
}

python configure_cron.py

echo "Setup complete."

# add python main.py to cron
