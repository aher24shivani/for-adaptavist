#!/bin/bash

# Check if a file path is provided as a command-line argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path="$1"

# Check if the file exists
if [ ! -f "$file_path" ]; then
    echo "Error: File not found - $file_path"
    exit 1
fi

# Word count using grep, tr, sort, and uniq
cat "$file_path" | tr -s '[:space:]' '\n' | grep -v '^\s*$' | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr
