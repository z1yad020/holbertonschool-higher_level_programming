#!/usr/bin/python3
"""Module for task 0"""


def lookup(obj):
    """return mapping proxy"""
    return list(dir(obj))


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

    def my_meth(self):
        pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
