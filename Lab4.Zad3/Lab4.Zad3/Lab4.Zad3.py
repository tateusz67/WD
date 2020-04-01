import sys

with open("zad3.txt", "w+") as plik:
    plik.writelines("Lorem ipsum dolor sit amet\nconsectetur adipiscing elit\nVivamus malesuada vitae felis vel sodales\n")

with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")