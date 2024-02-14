#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherit from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args):
        """update with *args"""
        ar = ["self.id", "self.width", "self.height", "self.x", "self.y"]
        for i, j in zip(ar, args):
            exec(f"{i} = {j}")

    def display(self):
        """display rectangle with default char"""
        x = "#" * self.__width

        for _ in range(self.__y):
            print()

        cor_x = " " * self.__x
        for _ in range(self.__height):
            print(cor_x, x, sep='')

    def area(self):
        """area of instance"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
