#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        print()
        return 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            print()
            return i
    print()
    return i + 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
