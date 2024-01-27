#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    i = tuple_a + (0, 0)
    j = tuple_b + (0, 0)

    return (i[0] + j[0], i[1] + j[1])


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
