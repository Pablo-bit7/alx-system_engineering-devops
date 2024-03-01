#!/usr/bin/env ruby

# Takes cmd line arg, finds & prints occurrences of the pattern "hbt" followed by 1 or more 't' chars
puts ARGV[0].scan(/hbt+n/).join

