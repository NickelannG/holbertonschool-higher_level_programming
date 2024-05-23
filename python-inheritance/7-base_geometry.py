#!/usr/bin/python3
"""
7-base_geometry:
    This module contains a base class BaseGeometry
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
        if not isinstance (value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
