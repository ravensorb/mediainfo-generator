#!/bin/bash

# Check if jq command is available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq command not found. Please install jq."; exit 1; }

# Get the directory path
directory="${1:-/data}"
output_file="${2:-mediainfo-summary.json}"

[[ ! -f "$directory/mediainfo.json" ]] && { echo 2>&1 "Could not find mediainfo.json.  Run generate first and then try again."; exit 1; } 

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
}]' $directory/mediainfo.json >> $directory/$output_file
