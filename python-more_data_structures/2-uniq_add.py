#!/usr/bin/python3
"""
Function Description:
This function that adds all unique integers in a list
(only once for each integer).

Parameters:
- my_list: the list

Return:
The result
"""


def uniq_add(my_list=[]):
    return sum(map(lambda x: x, set(my_list)))
