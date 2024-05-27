#!/usr/bin/python3
"""
6-load_from_json_file:
    This module contains the load_from_json_file function.
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a "JSON file"

    Parameters:
        - filename: The name of the JSON file

    Returns:
        - obj: the Python object created from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        obj = json.loads(f.read())
    return obj
