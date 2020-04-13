class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

    def czyjest(self):
        if(isinstance(self.imie,int)):
            print("Tak, imie to int")
        else:
            print("Nie, imie to nie int")


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

    def czypensja(self):
        if(isinstance(self.pensja,int)):
            print("Tak, pensja to int")
        else:
            print("Nie, pensja to nie int")

    def czypodklasa(self):
        if issubclass(Pracownik,Osoba):
            print("Pracownik to podklasa klasy Osoba")
        else:
            print("Pracownik nie jest podklasa klasy Osoba")


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

    def czypodklasa(self):
        if issubclass(Menadzer,Osoba):
            print("Menadzer to podklasa klasy Osoba")
        else:
            print("Menadzer nie jest podklasa klasy Osoba")


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.czyjest())
print(adrian.czypensja())

print(jozek.czypodklasa())
print(adrian.czypodklasa())