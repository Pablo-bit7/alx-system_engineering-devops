#!/usr/bin/env ruby

# Takes cmd line arg, matches strings that start with 'h' & end with 'n' (can have any single character in between)
puts ARGV[0].scan(/^h.n$/).join

