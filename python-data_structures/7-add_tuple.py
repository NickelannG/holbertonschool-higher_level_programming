#!/usr/bin/python3
"""
Adds 2 tuples

Function description:
This function takes two tuples with integers and adds the first two elements.
The first element should be the adition of the first element of each argument.
The second element should be the addition of the second element
of each argument.

Parameters:
2 tuples with integers:
- tuple_a
- tuple_b

Returns:
The added tuple with 2 integers
"""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
