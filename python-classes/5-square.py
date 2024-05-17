#!/usr/bin/python3
"""
5-square.py:
    This method contains a class Square that defines a square.

Classes:
    Square: A class that represents a square.

Methods:
    - size(getter): a method that retrieves the value of
    private attribute, size.
    - size(setter): a method that sets the value of private attribute, size.
    - area: A method within the Sqaure class
    that calculates the area of a square.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initialises Square with the given attributes.

        Parameters:
            size (int): A private instance attribute with a
            starting value of 0 and represents the size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """
        A getter method within the Square class that retrieves
        the value of private attribute, size.

        Returns:
            The private attribute, size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter method within the Sqaure class that sets the value of
        private attribute, size.

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
        A method within the Sqaure class that
        calculates the area of a square.

        Returns:
            int: The area of a square (size to the power of 2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        A method that prints in stdout the square with the # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
