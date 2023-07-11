#!/bin/bash

# Read input words into an array
read -ra words

# Declare an associative array to store word frequencies
declare -A frequencies

# Iterate over the words and count their frequencies
for word in "${words[@]}"; do
    ((frequencies[$word]++))
done

# Print words that appear exactly once
for word in "${!frequencies[@]}"; do
    if ((frequencies[$word] == 1)); then
        echo "$word"
    fi
done
