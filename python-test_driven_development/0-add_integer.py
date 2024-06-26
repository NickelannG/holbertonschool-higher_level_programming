#!/usr/bin/python3
"""
0-add_integer.py:
    This module contains the add_integer function
"""


def add_integer(a, b=98):
    """
    Returns a(int, float) + b(int, float).

    Raises:
        TypeError: if either a or b is not an integer or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a + b
