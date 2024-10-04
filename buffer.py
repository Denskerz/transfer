#!/bin/bash

# Check the number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_folder>"
    exit 1
fi

SOURCE_DIR="$1"
DEST_DIR="/path/to/archive"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Create a split archive directly without creating a full archive first
tar -czf - "$SOURCE_DIR" | split -b 10M - "$DEST_DIR/part_"

echo "Split archive parts created in $DEST_DIR"