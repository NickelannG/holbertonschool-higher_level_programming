#!/usr/bin/python3
"""
1-sqaure.py:
    This module shows a class "Sqaure" that defines a square.

Classes:
    Square: a class that represents a sqaure.
"""
class Square:
    """
    A class used to represent a sqaure.
    """
    def __init__(self, size):
        """
        Initialises Sqaure with the given attributes.
        
        Parameters:
            size: A private instance attribute that represents the size of a sqaure.
        """
        self.__size = size
