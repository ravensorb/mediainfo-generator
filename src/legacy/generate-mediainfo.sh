#!/bin/bash

# Check if the ffprobe command is available
command -v ffprobe >/dev/null 2>&1 || { echo >&2 "ffprobe command not found. Please install FFmpeg."; exit 1; }

# Check if jq command is available
command -v jq >/dev/null 2>&1 || { echo >&2 "jq command not found. Please install jq."; exit 1; }

# Get the directory path
[[ -z $PATH_DATA ]]     && PATH_DATA="${1:-/data}"
[[ -z $PATH_OUTPUT ]]   && PATH_OUTPUT="${2:-$PATH_DATA}"

ls -FCla $PATH_DATA

# Function to process a single file
process_file() {
    local input_file="$1"
    
    # Run ffprobe to get media information
    ffprobe_output=$(ffprobe -v quiet -print_format json -show_format -show_streams "$input_file")

    # Save the output to a JSON file
    local output_file="${input_file%.*}.json"
    [[ -f "$output_file" ]] && rm "$output_file"

    output_file="${input_file%.*}.mediainfo.json"
    echo "$ffprobe_output" > "$output_file"

    cat "$output_file" | jq '.format.filename |= sub("/data/"; "")' > "$output_file"

    echo "Media information saved to $output_file"
}

# Process all media files recursively
process_directory() {
    echo "Processing directory $1 and creating mediainfo files"
    local dir="$1"
    
    # Find all media files in the directory
    while IFS= read -r -d '' file; do
        # Process each file
        process_file "$file"
    done < <(find "$dir" -type f \( -iname "*.mp4" -o -iname "*.mkv" -o -iname "*.avi" -o -iname "*.m4v" -o -iname "*.mv4" \) -print0 | sort -z)
}

# Combine all JSON files into a single JSON file using jq
combine_json_files() {
    echo "Combining all JSON files into a single JSON file"
    local dir="$1"
    local combined_file="$2/mediainfo.json"
    local temp_combined_file="$2/temp_mediainfo.json"
    
    [[ -f "$temp_combined_file" ]] && rm "$temp_combined_file"
    [[ -f "$combined_file" ]] && rm "$combined_file"

    # Find all JSON files in the directory
    jq -s '.' "$dir"/**/*.mediainfo.json > "$temp_combined_file" || true

    # Check if jq encountered any errors
    if [ $? -eq 0 ]; then
        # If no errors, rename the temporary file to the final combined file
        mv "$temp_combined_file" "$combined_file"
        echo "Combined JSON file saved to $combined_file"
    else
        # If errors occurred, remove the temporary file
        rm "$temp_combined_file"
        echo "Error occurred while combining JSON files"
        exit 1
    fi
}

# Start processing the directory
process_directory "$PATH_DATA"

# Combine all JSON files
combine_json_files "$PATH_DATA" "$PATH_OUTPUT"
