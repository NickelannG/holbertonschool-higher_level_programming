#!/usr/bin/python3

"""
Function Description:
This function that replaces or adds key/value in a dictionary.
If a key exists in the dictionary, the value will be replaced.
If a key doesn’t exist in the dictionary, it will be created.

Parameters:
- a_dictionary: The dictionary
- key: the key to be added (will always be a string)
- value: the value to be added ( can be any type)
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    return a_dictionary
