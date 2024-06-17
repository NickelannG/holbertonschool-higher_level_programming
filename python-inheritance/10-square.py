#!/usr/bin/python3
"""
10-square:
    and a subclass square that inhertis from Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass of Rectangle class
    """
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__size ** 2

    def __str__(self):
        return str(Rectangle(self.__size, self.__size))
