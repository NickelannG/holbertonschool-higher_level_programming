#!/usr/bin/python3

"""
Function Description:
This function returns a list with all values multiplied by a number without
using any loops

Parameters:
- my_list: the list
- number: the number to multiply all the values with

Return:
a new list with the same length as my_list with each value multiplied
by the number
"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
