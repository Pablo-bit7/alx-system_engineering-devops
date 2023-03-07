#!/bin/bash

# Get the current working directory and its parent
CURRENT_DIR=$(pwd)
PARENT_DIR=$(dirname "$CURRENT_DIR")

# Copy each HTML file from the current directory to the parent directory
for file in *.html; do
	# Check if the file already exists in the parent directory and is newer
	if [ "$CURRENT_DIR/$file" -nt "$PARENT_DIR/$file" ]; then
		cp "$CURRENT_DIR/$file" "$PARENT_DIR"
		echo "Copied $file to $PARENT_DIR"
	else
		echo "Skipping $file"
	fi
done
