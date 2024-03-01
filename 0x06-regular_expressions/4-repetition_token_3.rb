#!/usr/bin/env ruby

# Takes cmd line arg, finds & prints occurrences pattern "hbt" followed by 0 or more 't' chars
puts ARGV[0].scan(/hbt*n/).join

