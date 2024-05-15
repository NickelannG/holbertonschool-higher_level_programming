#!/usr/bin/python3
"""
Function Description:
This function prints x elements of a list

Parameters:
- my_list: the list
- x: the number of elements to be printed

Return:
The real number of elements printed
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:   # if x is bigger than the len of my_list
            break
    print()
    return count
