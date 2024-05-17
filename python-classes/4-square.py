#!/usr/bin/python3
"""
4-square.py:
    This module shows a class that defines a square.

Classes:
    Sqaure: A class that represents a sqaure

Methods:
    - size (getter): A method to retrieve the value of
    private attribute, size.
    - size (setter): A method to set the value of private attribute size.
    - area: a method within the Square class that represents the area if a
    square.
"""


class Square:
    """
    A class used to represent a square.
    """
    def __init__(self, size=0):
        """
        Initialises Square with the given attributes.

        Parameters:
            size (int): A private instance atribute with a value of 0
            that represents the size of a square
        """
        self.__size = size

    @property
    def size(self):
        """
        A Getter method within the Square class that retrieves the value of
        private attribute, size.

        Returns:
            the private attribute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A Setter method that sets the value of private attribute, size.

        Parameters:
            value: the value to set size to

        Raises:
            TyperError: If value is not an integer.
            ValueError: If value is a negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        A method within the Square class that calculates
        the area of a square.

        Returns:
            int: The area of the square (size to the power of 2).
        """
        return self.__size ** 2
