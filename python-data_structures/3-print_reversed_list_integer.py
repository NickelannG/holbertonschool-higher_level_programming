#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(len(my_list)):
        my_list[i]
        print("{:d}".format(my_list[i]))
