#!/bin/bash

# Prompt the user to enter the path to a .txt file
read -p "Enter the path to the .txt file: " file_path

# Check if the provided file exists
if [ ! -f "$file_path" ]; then
    echo "Error: File not found - $file_path"
    exit 1
fi

# Word count using grep, tr, sort, and uniq
cat "$file_path" | tr -s '[:space:]' '\n' | grep -v '^\s*$' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr
