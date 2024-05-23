#!/usr/bin/python3
"""
8-rectangle:
    This module contains a base class BaseGeometry
    and a subclass Rectangle.
"""


class BaseGeometry:
    """
    Base class

    methods:
        - area
        - integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle that inherits from Base Class BaseGeometry
    """
    def __init__(self, width, height):                     
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
