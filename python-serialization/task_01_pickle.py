#!/usr/bin/python3
"""
task_01_pickle:
    This module contains the CustomObject class
"""
import pickle


class CustomObject:
    """
    This class defines a custom object

    Methods:
        - display: prints the object's attributes
        - serialize: serializes the current instance of the
        object using pickle.
        - deserialize: Class method that deserializes the current
        instance.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
