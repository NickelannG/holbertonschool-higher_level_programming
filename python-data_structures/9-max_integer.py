#!/usr/bin/python3

"""
Function description:
This function finds the biggest integers of a list

Parameters:
- my_list=[]: the list of integers we are looking through

Return:
The biggest integer in the list
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
