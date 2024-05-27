#!/usr/bin/python3
"""
3-to_json_string:
    This module contains the to_json_string function.
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string).

    Parameters:
        - my_obj: The python object to be converted

    Returns:
        - json_string: The JSON representation of the python object.
    """
    json_string = json.dumps(my_obj)

    return json_string
