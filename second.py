#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def writeThreeTimesToFile(filename, strng):
    try:
        with open(filename, "w") as fh:
            fh.write(strng * 3)
    except:
        pass

writeThreeTimesToFile("tree.txt", "apple")
