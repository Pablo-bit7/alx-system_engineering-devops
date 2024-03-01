#!/usr/bin/env ruby

# Takes cmd line arg, finds & prints occurrences of pattern "htn" (with optional 'b' and 't' characters in between)
puts ARGV[0].scan(/hb?t?n/).join

