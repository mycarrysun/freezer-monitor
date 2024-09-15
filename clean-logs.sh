#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(dirname "$0")"

DAYS_TO_KEEP=3

# Find and delete log files older than the specified number of days
find "$SCRIPT_DIR" -type f -name "*.log" -mtime +$DAYS_TO_KEEP -exec rm -f {} \;

echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted logs older than $DAYS_TO_KEEP days from $SCRIPT_DIR"
