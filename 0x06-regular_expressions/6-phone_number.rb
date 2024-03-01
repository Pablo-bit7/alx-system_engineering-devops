#!/usr/bin/env ruby

# Takes cmd line arg & matches for a 10-digit phone number
puts ARGV[0].scan(/^\d{10,10}$/).join

