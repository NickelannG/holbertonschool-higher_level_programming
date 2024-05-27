#!/usr/bin/python3
"""
1-write_file.py:
    This module contains the write_file function
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF-8) and returns the
    number of characters written

    Args:
        - filename: The name of the file to create/open
        - text: the string to write into the created/opened

    Returns:
        - num_chars: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
