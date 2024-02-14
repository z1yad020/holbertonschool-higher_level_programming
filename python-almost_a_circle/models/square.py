#!/usr/bin/python3
"""Module of Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """update with *args and **kwargs"""
        if not args:
            for i, j in kwargs.items():
                exec(f"self.{i} = {j}")
            return

        ar = ["self.id", "self.size", "self.x", "self.y"]
        for i, j in zip(ar, args):
            exec(f"{i} = {j}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
