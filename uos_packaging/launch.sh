#!/bin/bash

# DaoJiShi Launch Script
# Wrapper to handle environment variables and logging

APP_DIR="/opt/DaoJiShi"
EXECUTABLE="$APP_DIR/DaoJiShi"

# Set up logging directory in user's home
LOG_DIR="$HOME/.cache/DaoJiShi"
mkdir -p "$LOG_DIR"
LAUNCH_LOG="$LOG_DIR/startup.log"

echo "--- Launching DaoJiShi at $(date) ---" >> "$LAUNCH_LOG"

# Optional: Enable Qt Debugging if needed
# export QT_DEBUG_PLUGINS=1

# Ensure we are in the application directory (helps with relative paths if any remain)
cd "$APP_DIR" || { echo "Failed to cd to $APP_DIR" >> "$LAUNCH_LOG"; exit 1; }

# Run the application
# We redirect stdout and stderr to the log file
# Use system python3 to run the source code
python3 "$APP_DIR/run.py" "$@" >> "$LAUNCH_LOG" 2>&1

EXIT_CODE=$?
echo "--- Exited with code $EXIT_CODE at $(date) ---" >> "$LAUNCH_LOG"
exit $EXIT_CODE
