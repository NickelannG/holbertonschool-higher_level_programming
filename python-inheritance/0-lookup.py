#!/usr/bin/python3
"""
0-lookup:
    This module contains the lookup function
"""


def lookup(obj):
    """
    Returns a list of avaiblable attributes and methods of an object
    """
    return dir(obj)
