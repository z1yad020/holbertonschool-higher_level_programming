#!/usr/bin/python3
"""Example Google style docstrilank module, doing nothing"""


class Square:
    """The summary line for a class should fit on one line."""

    def __init__(self, size=0):
        """Initializes the instance based on args.

            Args:
              size: size of square"""

        self.__size = size


if __name__ == "__main__":
    """run as main"""
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
