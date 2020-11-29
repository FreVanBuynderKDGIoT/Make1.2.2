#!/usr/bin/env python
"""
een script waarbij je om input vraagt achter een willekeurig woord
en waarbij het script het woord achterstevoren weergeeft.
"""

# imports
from _datetime import datetime

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def get_word():
    word = str(input("which word do you wan to spell backward?: "))
    return word


def invert_word(word):
    inverted_word = "".join(reversed(word))
    return inverted_word


# functions
def main():
    try:
        word = get_word()
        inverted_word = invert_word(word)
        print("the word spelled backwards is:", str(inverted_word))

    except ValueError as err:
        print("Dit is geen juiste waarde: ", err)


if __name__ == '__main__':
    main()
