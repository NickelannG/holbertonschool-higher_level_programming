#!/usr/bin/python3
"""
2-matrix_divided.py:
    This module contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Returns:
        A new matrix(result) of all the numbers from a matrix input
        divided by an int or float (div), rounded to 2 decimal places.

    Raises:
         - TypeError: if matrix is not a list of lists of intergers / floats.
         - TypeError: if the rows of the matrix are not of the same size.
         - TypeError: if div is not an int or float
         - ZeroDivisionError: if div is 0.
    """
    result = []
    row_len = len(matrix[0])

    if (not isinstance(matrix, list) or
            not all(isinstance(i, list) for i in matrix)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        divided = [round(j / div, 2) for j in i]
        result.append(divided)
    return result
