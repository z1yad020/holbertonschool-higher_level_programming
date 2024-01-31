#!/usr/bin/python3

romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }


def roman_to_int(roman_string):
    result = 0
    if roman_string is None or type(roman_string) is not str:
        return result

    for c in range(len(roman_string) - 1):
        current = romans.get(roman_string[c])
        nextc = romans.get(roman_string[c + 1])

        if current < nextc:
            result += -current
        else:
            result += current

    return result + romans.get(roman_string[-1])


if __name__ == "__main__":
    """ Roman to Integer test file
    """
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
