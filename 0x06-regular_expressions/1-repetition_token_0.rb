#!/usr/bin/env ruby

# Takes cmd line arg, finds and print occurrences pattern "hbt" + 2-5 occurrences of 't'; followed by the letter 'n'.
puts ARGV[0].scan(/hbt{2,5}n/).join

