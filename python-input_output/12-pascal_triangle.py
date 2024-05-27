#!/usr/bin/python3
"""
12-pascal_triangle:
    This module contains the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing the
    Pascal's triangle of n

    Args:
        - n (int): the number of rows in the triangle.
    
    Returns:
        - The appended triangle list according to n.
    """
    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])  # first row

    # Outer loop iterate through rows
    for i in range(1, n):
        row = [1]  # First element of each row
        # Inner loop iterate through elements of each row
        for j in range(1, i):
            # Sum of two elements of prev row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row
        triangle.append(row)

    return triangle
