#!/usr/bin/python3
"""Module for task 7"""


class BaseGeometry:
    """ Base class of Geometry """
    def area(self):
        """dont now why exist"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
