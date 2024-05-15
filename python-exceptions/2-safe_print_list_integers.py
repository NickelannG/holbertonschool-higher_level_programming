#!/usr/bin/python3
"""
Function Description:
This function prints the first x elements of a list and only integers

Parameters:
- my_list: the list
- x: the number of elements to print

Returns:
the real number of integers printed
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                try:
                    print("{:d}".format(int(my_list[i])), end="")
                    count += 1
                except ValueError:
                    break
        except (IndexError, TypeError):
            break
    print()
    return count
