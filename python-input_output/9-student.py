#!/usr/bin/python3
"""
9-student:
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

    def to_json(self):
        """
        Returns a dictionary represenation of a Student instance
        """
        return self.__dict__
