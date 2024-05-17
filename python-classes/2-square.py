#!/usr/bin/python3
"""
2-sqaure.py:
    This module shows a class that defines sqaure.

Classes:
    Square: a class that represents a square.
"""


class Square:
    """
    A class used to represent a square.
    """
    def __init__(self, size=0):
        """
        Initialises Sqaure with the given attributes.

        Parameters:
            size (int): a private instance attribute that represents
            the size of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is a negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
