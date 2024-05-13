#!/usr/bin/python3
""" prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    result = ""
    if not matrix:
        return result
    for i in range(len(matrix)):  # rows
        for j in range(len(matrix[i])):  # elements in each row
            result += "{:d}".format(matrix[i][j])
            if j < len(matrix[i]) - 1:
                result += " "
        if i < len(matrix) - 1:
            result += "\n"
    print("{}".format(result))