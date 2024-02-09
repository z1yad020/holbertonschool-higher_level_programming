#!/usr/bin/python3
"""Module for task 3"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class ; otherwise False"""
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
