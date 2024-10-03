#!/bin/bash

# Prompt for the folder path
read -p "Enter the path to the folder for archiving: " folder_path

# Prompt for the remote server address
read -p "Enter the remote server address: " remote_server

# Prompt for the folder path on the remote server to save the archive
read -p "Enter the path to the folder on the remote server to save the archive: " remote_folder

# Archive the folder and split into 10 parts
ssh "$remote_server" "tar -czf - '$folder_path' | split -b 10M - '${remote_folder}/archive_part_'"

# Exit from the remote server (ssh will automatically close after the command)

# Copy the necessary files to Windows
# Make sure you have WinSCP or another SCP client installed
read -p "Enter the path to the files on the remote server to copy: " remote_files_path
read -p "Enter the path on your computer to save the files: " local_save_path

# Use WinSCP to copy files
winscp.com /command "open sftp://$remote_server" "get '$remote_files_path/*' '$local_save_path'" "exit"