#!/usr/bin/python3

"""
Print square
"""


def print_square(size):
    """
    Print square
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    x = size * '#'
    [print(x) for i in range(size)]
