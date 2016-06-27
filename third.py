#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Write unittests for this function:

def count_letter_in_string(string, letter):
  if type(string) != str:
    return 0
  count = 0
  for current_letter in string:
    if current_letter == letter:
      count += 1
  return count
