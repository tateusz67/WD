import sys

with open("plik.txt", "r+") as f:
    data = f.read()
    lista = data.split(" ")
    f.write("\n")
    f.write("\n".join(map(str, lista)))
