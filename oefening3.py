#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
"""

# imports


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# functions


def make_guesslist():
    programmed_list = ["zero", "one", "two", "three", "four', 'five", "six", "seven", "eight", "nine"]
    return programmed_list

def main():
    guess = input("which word do you think is in the list?: ")
    if guess in make_guesslist():
        print("""the word "{0}" was found in the list""".format(guess))


if __name__ == '__main__':
    main()
