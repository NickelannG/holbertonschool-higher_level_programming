#!/usr/bin/python3
"""
10-student:
    This module contains the Student class.
"""


class Student:
    """
    This class defines a student.

    Attributes:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary represenation of a Student instance
        """
        if attrs is not None:
            if all(isinstance(i, str) for i in attrs):
                filtered_dict = {}
                for attr in attrs:
                    if attr in self.__dict__:
                        filtered_dict[attr] = self.__dict__[attr]
                return filtered_dict
        else:
            return self.__dict__
