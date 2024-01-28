#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def mycalc():
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opcodes = (('+', add), ('-', sub), ('*', mul), ('/', div))

    for i, j in opcodes:
        if i == argv[2]:
            result = j(int(argv[1]), int(argv[3]))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))


if __name__ == "__main__":
    mycalc()
