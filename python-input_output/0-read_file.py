#!/usr/bin/python3


"""Module"""


def read_file(filename=""):
    """function"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
