#!/usr/bin/python3
"""
5-text_indentation.py:
    This module contains the text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters ., ?, and :

    Parameters:
        - text (str): the text to be printed

    Raises:
        TypeError: If text is not a string.
    """

    chars = ['.', '?', ':']
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        result += char
        if char in chars:
            result += "\n\n"

    lines = result.split('\n')
    for line in lines:
        print(line.strip())
