#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix
    """

    newList = []
    z = 0

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    ln = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(row) != ln:
            raise TypeError("Each row of the matrix must have the same size")

        newList.append([])
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            newList[z].append(round(i / div, 2))
        z += 1

    return newList


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrix_divided(matrix, 3))
