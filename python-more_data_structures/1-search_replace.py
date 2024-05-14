#!/usr/bin/python3
"""
Function description:
A function that replaces all occurrences of an element by another
in a new list.

Parameters:
- my_list: The initial list
- search: The element to replace in the list
- replace: The new element


Returns:
The modified list
"""


def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))
