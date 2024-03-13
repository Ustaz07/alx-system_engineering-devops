#!/usr/bin/env ruby

def extract_format(input)
  match_data = input.match(/from:(\w+)|to:(\w+)|flags:([0-9:-]+)/)
  match_data ? match_data.captures.compact.join(',') : ''
end

input_string = ARGV[0]
puts extract_format(input_string)
