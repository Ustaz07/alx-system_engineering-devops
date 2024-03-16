#!/usr/bin/env ruby

def match_school(string)
  regex = /School/
  matches = string.scan(regex)
  matches.join('')
end

input_string = ARGV[0]
result = match_school(input_string)

puts result
