#!/usr/bin/python3
"""
task_03_countediterator:
    This module contains the CountedIterator class.
"""


class CountedIterator:
    """
    Extends the built-in iterator and keeps a count of the items that
    have been iterated over.
    """
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter
