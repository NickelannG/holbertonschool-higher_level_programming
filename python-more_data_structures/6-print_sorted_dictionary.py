#!/usr/bin/python3

"""
Function Description:
This function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = (sorted(a_dictionary.keys()))
    for key in sorted_keys:
        print(key, ":", a_dictionary[key])
