#!/usr/bin/python3

"""
Function description:
This function returns a key with the biggest integers value
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
