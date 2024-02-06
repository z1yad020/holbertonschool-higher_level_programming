#!/usr/bin/python3
"""
Module of Rectangle

Adding Area and Perimeter

String representation

Eval is magic

Detect instance deletion
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

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: \
           {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
