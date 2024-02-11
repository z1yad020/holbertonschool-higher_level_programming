#!/usr/bin/python3


"""Module"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    y = []
    x = [1]
    result = []
    for i in range(1, n + 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                y.append(1)
            else:
                y.append(x[j] + x[j - 1])
        result.append(y)
        x = y
        y = []
    return result


def print_triangle(triangle):
    """Print the triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(10))
