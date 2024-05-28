#!/usr/bin/python3
"""
task_00_basic_serialization:
    This module contains the serialize_and_save_to_file
    and load_and_deserialize functions.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This function serializes a Python dictionary to a JSON file

    Parameters:
        - data: A Python Dictionary with data
        - filename: The filename of the output JSON file.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    This function deserializes the JSON file to recreate the Python
    dictionary.

    Parameters:
        - filename: The filename of the input JSON file.

    Returns:
        - A Python diciontary with the deseialized JSON data from the
        file.
    """
    with open(filename) as f:
        python_dict = json.loads(f.read())
    return python_dict
