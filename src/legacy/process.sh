#!/bin/bash

# Check if jq command is available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq command not found. Please install jq."; exit 1; }

option="" # Default option

while getopts "gs" opt; do
  case $opt in
    g)
      #echo "Requested to generate mediainfo files"
      option="g"
      shift 1
      ;;
    s)
      #echo "Requested to summarize mediainfo files"
      option="s"
      shift 1
      ;;
    \?)
      # Invalid option
      echo "Invalid option: -$OPTARG"
      echo "Usage: ./process.sh [-g|-s] [ARGUMENTS]"
      exit 1
      ;;
  esac
done

[[ -z $option ]] && option="g"

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
