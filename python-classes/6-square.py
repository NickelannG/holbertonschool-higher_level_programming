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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises Square with the given attributes.

        Parameters:
            - size (int): A private isntance attribute that has a starting
            value of 0 and represents the size of a square.
            - position: (tuple): a private instance attribute that has a
            starting value of (0, 0) and represents the position of
            the square.

        Raises:
            TyperError: If position is not a tuple of 2 positive
            integers.
        """
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(position[0], int) or
                not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__position = position

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

    @property
    def position(self):
        """
        A getter method that retrieves the value of position.

        Returns:
            the private attribute, position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        A setter method that sets the value of private attribute,
        position.

        Parameters:
            value (tuple): the value to set position to.

        Raises:
            TyperError: If value is not a tuple of 2 positive
            integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        with the # character according to size and position.

        Returns:
            nothing if the size is 0
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" "*self.__position[0] + "#"*self.__size)
