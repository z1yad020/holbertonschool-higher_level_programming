#!/usr/bin/python3

def uppercase(str):
    x = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            x += chr(ord(c) - 32)
            continue
        x += c
    print(x.format())


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
