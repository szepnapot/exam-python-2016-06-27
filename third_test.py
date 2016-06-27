#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from third import count_letter_in_string

class LetterCountTest(unittest.TestCase):

  def test_emptyStringInput_withLetter(self):
    self.assertEqual(count_letter_in_string('', 'a'), 0)

  def test_emptyArguments(self):
    self.assertEqual(count_letter_in_string('', ''), 0)

  def test_allLettersSame(self):
    self.assertEqual(count_letter_in_string('aaaaa', 'a'), 5)

  def test_inputLetterNotInString(self):
    self.assertEqual(count_letter_in_string('bbbbbb', 'c'), 0)

  def test_caseSensitivity(self):
    self.assertEqual(count_letter_in_string('AaAaA', 'A'), 3)

  def test_longStringCompare_withBuiltIn(self):
    from collections import Counter
    longString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    letter_l_counter = Counter(longString)['l']
    self.assertEqual(count_letter_in_string(longString, 'l'), letter_l_counter)

if __name__ == '__main__':
	unittest.main()
