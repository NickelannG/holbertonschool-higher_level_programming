#!/usr/bin/python3
"""
1-rectangle:
    The module contains the class, Rectangle that defines a rectangle
"""


class Rectangle:
    """
    This class is used to define a rectangle

    Attributes:
        - number_of_instances: to keep track of the number of instances
        - print_symbol: Used as a symbol for string representation
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
