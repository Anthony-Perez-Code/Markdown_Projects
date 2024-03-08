#!/bin/bash

# Prompt the user for a number
read -p "Enter the number of files to create: " num_files

# Validate input (ensure it's a positive integer)
if ! [[ "$num_files" =~ ^[1-9][0-9]*$ ]]; then
    echo "Invalid input. Please enter a positive integer."
    exit 1
fi

# Create empty files
for ((i = 1; i <= num_files; i++)); do
    touch "file$i.txt"
done

# Display a message
echo "$num_files empty files created: file1.txt, file2.txt, ..., file$num_files.txt"
