#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.items()):
        print("{}: {}".format(i[0], i[1]))



if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
