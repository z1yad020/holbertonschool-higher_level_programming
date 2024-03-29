#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_squares_output = Square.load_from_file()

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
