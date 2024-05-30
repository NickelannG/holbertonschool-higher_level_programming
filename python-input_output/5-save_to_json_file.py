#!/usr/bin/python3
"""
5-save_tp_json_file:
    This module contains the save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file,
    using a JSON representation.

    Parameters:
        - my_obj: The object to convert to JSON string.
        - filename: The name of the file to open or create.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(my_obj, f)

    except PermissionError as e:
        print(f"[PermissionError] {e}")

    except TypeError as e:
        print(f"[TypeError] {e}")
