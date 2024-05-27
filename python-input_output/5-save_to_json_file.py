#!/usr/bin/python3
"""
5-save_tp_json_file:
    This module contains the save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file,
    using a JSON repreentation.

    Parameters:
        - my_obj: the object to convert to JSON string.
        - filename: the name of the file to open or create
    """
    json_string = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_string)
