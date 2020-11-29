#!/usr/bin/env python
"""
Een script dat:
Stel dat je een lijst met lijsten hebt waar elke waarde in de binnenste lijsten een tekenreeks is, zoals deze:
lijst = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
Je kunt het raster[x][y] zien als het karakter op de x- en y-coördinaten van een "plaatje"
dat met tekstkarakters is getekend. De (0, 0) oorsprong zal in de linkerbovenhoek liggen, de x-coördinaten nemen toe
naar rechts, en de y-coördinaten nemen toe naar beneden.
Neem bovenstaande lijst mee over en zorg voor de volgende output:
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

en ook deze:

....O....
...OOO...
..OOOOO..
.OOOOOOO.
.OOOOOOO.
..OO.OO..
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"



def make_list():
    list = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    return list


def turn_clockwise(list):
    turned_list_clockwise = zip(*list[::-1])
    return turned_list_clockwise



def print_clockwise_list():
    print("\n".join(map("".join, turn_clockwise(make_list()))))


def main():
    print_clockwise_list()
    print("\nEn ook deze\n")
    print("sorry, voor deze vind ik geen oplossing")


if __name__ == '__main__':
    main()
