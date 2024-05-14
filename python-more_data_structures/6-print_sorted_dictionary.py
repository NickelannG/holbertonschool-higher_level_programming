#!/usr/bin/python3

"""
Function Description:
This function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = (sorted(a_dictionary.keys()))
    if sorted_keys:
        format = map(lambda key: f"{key}: {a_dictionary[key]}", sorted_keys)
        print(*format, sep='\n')
