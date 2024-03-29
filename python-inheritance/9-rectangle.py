#!/usr/bin/python3
""" Module for task 9"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ ractangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(
                self.__class__.__name__,
                self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
