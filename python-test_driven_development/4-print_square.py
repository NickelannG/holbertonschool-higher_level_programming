#!/usr/bin/python3
"""
4-print_square:
    This module contains the print_square function
"""


def print_square(size):
    """
    Prints a sqaure with the '#' character

    Parameter:
        - size: The length of the square
    Raises:
        - TypeError: If size is not an int
        - TypeError: If size is less than 0
        - ValueError: If size is a float and is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#'*size)
