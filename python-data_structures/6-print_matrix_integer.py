#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        ln = len(matrix[i])
        for j in range(ln):
            print("{}".format(matrix[i][j]), end='')
            if j != ln - 1:
                print(" ".format(), end='')
        print("".format())


if __name__ == "__main__":
    matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
