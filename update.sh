#!/usr/bin/env bash
set -euo pipefail

git checkout main || git checkout -b main origin/main
git pull -r
./install.sh