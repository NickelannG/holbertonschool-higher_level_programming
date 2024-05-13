#!/usr/bin/python3
"""
Function description:
This function returns a tuple with the length of a string and its first
character.

Parameters:
- sentence: the string
"""


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)


sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
