#!/usr/bin/python3
"""task 6"""


class Square:
    """The summary line for a class should fit on one line."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance based on args."""
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print(self.__position[1] * "\n", end="")

        if self.__size == 0:
            print()
        else:
            x = self.__size * '#'
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
                print(x)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, ('1', 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
