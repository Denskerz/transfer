#!/bin/bash

# Check the number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_folder>"
    exit 1
fi

SOURCE_DIR="$1"
DEST_DIR="/path/to/archive"
ARCHIVE_NAME="archive.tar.gz"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Create the archive
tar -czf "$DEST_DIR/$ARCHIVE_NAME" "$SOURCE_DIR"

# Split the archive into parts of 10MB
split -b 10M "$DEST_DIR/$ARCHIVE_NAME" "$DEST_DIR/part_"

echo "Archived and split into parts in $DEST_DIR"