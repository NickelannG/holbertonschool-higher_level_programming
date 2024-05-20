#!/usr/bin/python3
"""
3-say_my_name:
    This module contains the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints my name is <first name> <last name>

    Parameters:
        - first_name (str): the first name
        - last_name (str): the last name

    Raises:
        - TypeError: if first name is not a string
        - TypeError: if last-name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
