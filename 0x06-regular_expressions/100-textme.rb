#!/usr/bin/env ruby

def extract_format(input)
  match_data = input.match(/\[from:(?:\w+|\+\d+)\] \[to:(?:\w+|\+\d+)\] \[flags:(?:-?\d+:)+-?\d+\]/)
  match_data ? match_data.to_s.gsub(/\[from:|\[to:|\[flags:|\]/, '').gsub(':', ',') : ''
end

input_string = ARGV[0]
puts extract_format(input_string)
