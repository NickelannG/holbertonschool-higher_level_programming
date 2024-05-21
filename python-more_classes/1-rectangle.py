#!/usr/bin/python3
"""
1-rectangle:
    The module contains the class, Rectangle that defines a rectangle
"""


class Rectangle:
    """
    This class is used to define a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialises class Rectangle with the given attributes.

        Parameters:
            - width (int): Private instance attribute that represents
            the width of rectangle.
            - height (int): Private instance attribute that represents the
            height of rectangle.

        Raises:
            - TypeError: if width or height is not an int
            - ValueError: if width or height is a negative int
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
