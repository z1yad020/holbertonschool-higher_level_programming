#!/usr/bin/python3
"""
Module of Rectangle

Adding Area and Perimeter

String representation
"""


class Rectangle():
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if 0 in [self.__height, self.__width]:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        if 0 in [self.__height, self.__width]:
            return ""

        prt = ""
        line = self.__width * "#"
        for i in range(self.__height - 1):
            prt += line + "\n"
        prt += line
        return prt


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: \
           {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
