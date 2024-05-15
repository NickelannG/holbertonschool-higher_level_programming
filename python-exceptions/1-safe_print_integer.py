#!/usr/bin/python3
"""
Function Description:
This function prints an integer with "{:d}".format()

Parameters:
- value: can be any type (integer,string etc)

Returns:
True if value has been correctly printed, otherwise False
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
