#!/usr/bin/python3
import hidden_4


def func():
    x = dir(hidden_4)

    for i in range(len(x)):
        if (x[i])[:2] != "__":
            print(x[i])


if __name__ == "__main__":
    func()
