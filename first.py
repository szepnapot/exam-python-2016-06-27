#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

def geteverySecondElement(lista):
    if type(lista) != list:
        raise TypeError
    else:
        return [i for i in range(1, len(lista)) if i % 2 == 0]


print(geteverySecondElement([[1, 2, 3, 4, 5]]))
