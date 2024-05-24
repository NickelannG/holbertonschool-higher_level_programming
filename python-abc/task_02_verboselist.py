#!/usr/bin/python3
"""
task_02_veroselist:
    This module contains a class Verbose list that inherits the Python
    built-in list class
"""


class VerboseList(list):
    """
    A class that overrides the append, extend, remove,
    and pop methods to modify a list
    """
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        num = len(items)
        print(f"Extended the list with [{num}] items.")

    def remove(self, item):
        if item not in self:
            print(f"[{item}] not found in list")
        else:
            print(f"Removed [{item}] from the list.")
            super().remove(item)

    def pop(self, idx=None):
        if idx is None:
            idx = len(self) - 1
        item = super().pop(idx)
        print(f"Popped [{item}] from the list.")
        return (item)
