#!/usr/bin/env ruby

def extract_format(input)
  match_data = input.match(/\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/)
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]
  "#{sender},#{receiver},#{flags}"
end

input_string = ARGV[0]
puts extract_format(input_string)
