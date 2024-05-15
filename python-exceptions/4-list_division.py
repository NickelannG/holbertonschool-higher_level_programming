#!/usr/bin/python3

"""
Function Description:
This function divides element by element 2 lists

Parameters:
- my_list_1: the first list - can contain any type
- my_list_2: the second list - can contain any type
- list_length - can be bigger than the lenght of both lists

Return:
a new list (length = list_length) with all divisions
"""


def list_division(my_list_1, my_list_2, list_length):
    res = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    print("out of range")
                    res.append(0)
                    continue
                if (not isinstance(my_list_1[i], (int, float)) or
                        not isinstance(my_list_2[i], (int, float))):
                    print("wrong type")
                    res.append(0)
                    continue
                res.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                res.append(0)
    except IndexError:
        print("out of range")
        res.append(0)
    finally:
        return res
