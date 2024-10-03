#!/bin/bash

# Prompt for the folder path to archive
read -p "Enter the path to the folder to archive: " folder_path

# Check if the folder exists
if [ ! -d "$folder_path" ]; then
    echo "Folder not found. Please check the path."
    exit 1
fi

# Prompt for the output folder path
read -p "Enter the path to the folder to save the archives: " output_path

# Check if the output folder exists
if [ ! -d "$output_path" ]; then
    echo "Output folder not found. Creating the folder..."
    mkdir -p "$output_path"
fi

# Create the archive
archive_name="archive.zip"
zip -r "$output_path/$archive_name" "$folder_path"

# Split the archive into parts of 10 MB
split -b 10M "$output_path/$archive_name" "$output_path/${archive_name%.zip}-part_"

# Optionally remove the original archive
# rm "$output_path/$archive_name"

echo "Archiving and splitting completed. Archives saved in $output_path."