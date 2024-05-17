#!/usr/bin/python3
"""
6-square.py:
    This module contains a class Square that defines a square.
    
Classes:
    Square: represents a square.
    
Methods:
    - size(getter): A method that retrieves the value of
    private attribute, size.
    - size(setter): A method that sets the value of
    private attribute, size.
    - area: A method that calculates the area of a square.
    - my_print: A method that prints a square with the # character.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initialises Square with the given attributes.
        
        Parameters:
            size (int): A private isntance attribute that has a starting
            value of 0 and represents the size of a square.
        """
        self.__size = size
    
    @property
    def size(self):
        """
        A getter method within the Square class that retrieves the
        private attribute, size.
        
        Returns:
            The private attribute, size.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        A setter method within the Square class that sets a value to
        the private attribute, size.
        
        Parameters:
            value: the value to set size to.
            
        Raises:
            TypeError: If value is not an integer.
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
            int: the area of a square (size to the power of 2).
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        A method within the Square class that prints in stdout a square
        with the # character according to size.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#"*self.__size)