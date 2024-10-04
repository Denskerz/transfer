#!/bin/bash

# Prompt the user for the path to the folder
read -p "Enter the path to the folder to archive: " SOURCE_DIR
DEST_DIR="/path/to/archive"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: The specified folder '$SOURCE_DIR' does not exist."
    exit 1
fi

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

echo "Creating split archive from '$SOURCE_DIR'..."

# Create a split archive directly without creating a full archive first
if tar -czf - "$SOURCE_DIR" | split -b 10M - "$DEST_DIR/part_"; then
    echo "Split archive parts created successfully in '$DEST_DIR'."
else
    echo "Error: Failed to create the archive."
    exit 1
fi

# Optional: List the created parts
echo "Created parts:"
ls -lh "$DEST_DIR/part_"*