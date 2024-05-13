#!/usr/bin/python3

"""
Function description:
This function finds all multiples of 2 in a list

Parameters:
- my_list=[]: the list

Return:
A new list with True or False, depending on whether the integer at the same
position in the original list is a multiple of 2
"""


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None

    result = []
    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
