#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def geteverySecondElement(lista):
    if type(lista) == list:
        return [i for i in range(1, len(lista)) if i % 2 == 0]
    raise Exception('A very specific bad thing happened....input is not a list, meh')

print(geteverySecondElement([1, 2, 3, 4, 5]))
print(geteverySecondElement(2))
