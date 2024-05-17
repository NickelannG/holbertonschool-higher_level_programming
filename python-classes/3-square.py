#!/usr/bin/python3
"""
3-square.py:
    This module shows a class that defines a square.

Classes:
    Square: a class that represents a square.

Methods:
    area: this method represents the area of a square
"""


class Square:
    """
    A class used to represent a sqaure.
    """
    def __init__(self, size=0):
        """
        initialises Square with the given attributes.

        Parameters:
            size (int): A private instance attribute with a value of 0
            that represents the size of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is a negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        A method within the Square class that
        calculates the current square area.

        Returns:
            size to the power of 2.
        """
        return self.__size ** 2
