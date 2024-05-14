#!/usr/bin/python3

"""
Function Description:
This function deletes a key in a dictionary.
If a key doesnt exist, the dictionary wont change.
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
        return a_dictionary
    return a_dictionary
