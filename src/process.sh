#!/bin/bash

# Check if jq command is available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq command not found. Please install jq."; exit 1; }

option="g" # Default option

while getopts ":gs:" opt; do
  case $opt in
    g)
      option="g"
      ;;
    s)
      option="s"
      ;;
    \?)
      # Invalid option
      echo "Invalid option: -$OPTARG"
      echo "Usage: ./process.sh [-g|-s] [ARGUMENTS]"
      exit 1
      ;;
  esac
done

shift 1 # Shift the command line arguments

# Run the script based on the selected option
case $option in
  g)
    echo "Running process script..."
    ./generate-mediainfo.sh "$@"
    ;;
  s)
    echo "Running summarize script..."
    ./summarize-mediainfo.sh "$@"
    ;;
esac
