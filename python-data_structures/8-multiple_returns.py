#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)

    if x == 0:
        return (x, None)

    return (x, sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
