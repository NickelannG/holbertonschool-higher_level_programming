#!/usr/bin/python3
"""
Function Description:
This function divides 2 integers and prints the result

Returns:
The value of the division, otherwise, None
"""


def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res))
    return res
