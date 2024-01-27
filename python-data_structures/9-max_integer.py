#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    mx = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > mx:
            mx = my_list[i]
    return mx


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
