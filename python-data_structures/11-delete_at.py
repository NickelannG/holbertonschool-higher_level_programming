#!/usr/bin/python3

"""
Function Description:
This function deletes an item at a specific position in a list
without using the pop() function

Parameters:
- my_list=[]: the list
- idx=0: the index of the item to be removed

Returns:
The new list after the item has been removed
"""


def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return []

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
