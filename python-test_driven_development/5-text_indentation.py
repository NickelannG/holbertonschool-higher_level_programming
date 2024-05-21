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
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            while (i + 1) < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
