#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = a_dictionary.copy()
    for k, v in x.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
