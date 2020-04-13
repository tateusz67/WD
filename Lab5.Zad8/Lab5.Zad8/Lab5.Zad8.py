class Samogloski:
    def __init__(self, wyraz,smgloski):
        self.wyraz = wyraz
        self.smgloski = smgloski

    def __iter__(self):
        return self

    def __next__(self):
        wynik = [each for each in self.wyraz if each in self.smgloski] 
        return wynik 


iter = Samogloski("testowy", "AaEeIiOoUuYy")
print(iter)
print(next(iter))

iter2 = Samogloski("Samogloska", "AaEeIiOoUuYy")
print(iter2)
print(next(iter2))

