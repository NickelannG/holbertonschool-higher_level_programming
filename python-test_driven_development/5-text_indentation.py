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
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i < len(text):
        result += text[i]
        if text[i] in chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    lines = result.split('\n')
    for line in lines:
        print(line.strip())
