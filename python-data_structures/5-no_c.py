#!/usr/bin/python3

def no_c(my_string):
    x = list(my_string)

    for i in range(len(x) - 1, -1, -1):
        if x[i] == 'c' or x[i] == 'C':
            del x[i]

    return ''.join(x)


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
