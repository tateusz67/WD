class Material:
    # definicja konstruktora
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyświetl_nazwę(self):
        return self.rodzaj


class Ubrania(Material):
    # definicja konstruktora
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyświetl_dane (self):
        return self.rozmiar, self.kolor, self.dla_kogo

class Sweter(Ubrania):
    # definicja konstruktora
    def __init__(self,rodzaj_swetra ):
        self.rodzaj_swetra  = rodzaj_swetra

    def wyświetl_dane (self):
        return self.rodzaj_swetra



material = Material("bawelna", 12, 5)

print(material.wyświetl_nazwę())

sweterBawelniany = Sweter("golf")
print(sweterBawelniany.wyświetl_dane())


