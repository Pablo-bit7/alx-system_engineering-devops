#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Define the regex pattern to match "School"
pattern = /School/

# Find all matches in the input string
matches = input_string.scan(pattern)

# Check if matches are found
if !matches.empty?
  # Concatenate all matches without spaces
  result = matches.join('')
  puts result
end

