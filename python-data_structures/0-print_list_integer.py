#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))


if __name__ == "__main__":
    my_list = [1, 54, 8]
    print_list_integer(my_list)
