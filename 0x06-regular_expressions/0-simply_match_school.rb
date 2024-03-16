#!/usr/bin/env ruby

def match_school(string)
  regex = /Schoool/
  string.scan(regex)
end

input_string = ARGV[0]
results = match_school(input_string)

results.each { |result| puts result }
