#!/usr/bin/python3
"""
1-my_list:
    This module contains a class Mylist with the print_sorted function
"""


class MyList(list):
    def print_sorted(self):
        """
        prints the sorted list (ascending)
        """
        print(sorted(self))
