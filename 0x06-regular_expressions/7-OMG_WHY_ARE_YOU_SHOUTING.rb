#!/usr/bin/env ruby

# Takes cmd line arg, finds & prints sequences of uppercase letters
puts ARGV[0].scan(/[A-Z]*/).join

