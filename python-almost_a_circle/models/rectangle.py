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

    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        self.__dict__[f"__{name}"] = value


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    print(r1.__dict__)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
