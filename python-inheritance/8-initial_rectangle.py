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
        if type(value) is not int:
            raise TypeError("{0} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{0} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle that inherits from Base Class BaseGeometry
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)


        self.__width = width
        self.__height = height
