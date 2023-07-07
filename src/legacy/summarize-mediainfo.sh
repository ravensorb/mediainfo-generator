#!/bin/bash

# Check if jq command is available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq command not found. Please install jq."; exit 1; }

# Get the PATH_DATA path
[[ -z $PATH_DATA ]]   && PATH_DATA="${1:-/data}"
[[ -z $PATH_OUTPUT ]] && PATH_OUTPUT="${1:-/data}"
[[ -z $FILE_OUTPUT ]] && FILE_OUTPUT="${2:-$PATH_OUTPUT/mediainfo-summary.json}"
[[ -z $FILE_INPUT ]]  && FILE_INPUT="${PATH_DATA}/mediainfo.json"

[[ ! -f "$PATH_DATA/mediainfo.json" ]] && { echo 2>&1 "Could not find mediainfo.json.  Run generate first and then try again."; exit 1; } 

echo "Summarizing mediainfo files in $FILE_OUTPUT"
[[ -f "$FILE_OUTPUT" ]] && rm "$FILE_OUTPUT"

jq '[.[] | {
  "filename": .format.filename,
  "format": {
    "format_name": .format.format_name,
    "format_long_name": .format.format_long_name,
    "bit_rate": .format.bit_rate,
    "size": .format.size,
    "encoder": .format.tags.encoder,
  },
  "video": {
    "codec_name": .streams[0].codec_name,
    "codec_long_name": .streams[0].codec_long_name,
    "profile": .streams[0].profile,
    "codec_type": .streams[0].codec_type,
    "coded_width": .streams[0].coded_width,
    "coded_height": .streams[0].coded_height,
    "avg_frame_rate": .streams[0].avg_frame_rate
  },
  "audio": {
    "codec_name": .streams[1].codec_name,
    "codec_long_name": .streams[1].codec_long_name,
    "profile": .streams[1].profile,
    "codec_type": .streams[1].codec_type,
    "sample_rate": .streams[1].sample_rate,
    "channels": .streams[1].channels,
    "channel_layout": .streams[1].channel_layout
  }
}]' $FILE_INPUT >> $$FILE_OUTPUT
