#!/usr/bin/env ruby

# Takes cmd line arg, extract info from text string & prints it separated by commas
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

