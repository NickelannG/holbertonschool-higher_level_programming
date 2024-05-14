#!/usr/bin/python3
"""
Function description:
This function converts a roman numeral to an integer

Return:
An integer.
if roman_string is not a string or None, return 0
"""


def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    for i in str(roman_string):
        if i not in my_dict.keys():
            return 0
    num = my_dict[roman_string[-1]]
    for i in range(len(roman_string) - 2, -1, -1):
        if my_dict[roman_string[i]] >= my_dict[roman_string[i+1]]:
            num += my_dict[roman_string[i]]
        else:
            num -= my_dict[roman_string[i]]
    return num
