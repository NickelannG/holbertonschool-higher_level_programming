#!/usr/bin/python3
"""
4-from_json_string:
    This module contains the from_json_string function.
"""
import json


def from_json_string(my_str):
    """
    This function retuns an object represented by a JSON string.

    Parameters:
        - my_str: The JSON string to be converted.

    Returns:
        - python_obj: The object (Python data structure).
    """
    python_obj = json.loads(my_str)

    return python_obj
