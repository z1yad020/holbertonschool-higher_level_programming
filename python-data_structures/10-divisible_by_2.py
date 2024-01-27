#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)
