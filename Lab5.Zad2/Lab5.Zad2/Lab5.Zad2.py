class Kwadrat:

    def __init__(self, a, b): 
        self.a = a 
        self.b = b 

    def __add__(self, druga): 
        return self.a + druga.a, self.b + druga.b 
        
kw1 = Kwadrat(5,5)
kw2 = Kwadrat(4,4)

kw3 = kw1 + kw2
print(kw3)