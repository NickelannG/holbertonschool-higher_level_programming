#!/usr/bin/python3
"""
2-append_write.py:
    This module contains the append_write function.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file (UTF8).

    Args:
        - filename (str): the name of the file to be opened or created.
        - text (str): The string used to append the opened or
        created file.

    Returns:
        - num_chars: the number of characters in the appended file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
