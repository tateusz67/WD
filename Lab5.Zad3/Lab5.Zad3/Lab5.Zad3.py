class Liczba: 
    def __init__(self, a): 
        self.a = a 
    def __ge__(self, druga): 
        if(self.a>=druga.a): 
            print(self.a, " >= ",druga.a) 
        else: 
            print(self.a, " < ",druga.a) 

    def __gt__(self, druga): 
        if(self.a>druga.a): 
            print(self.a, " > ",druga.a) 
        else: 
            print(self.a, " < ",druga.a) 

    def __le__(self, druga): 
        if(self.a<=druga.a): 
            print(self.a, " <= ",druga.a) 
        else: 
            print(self.a, " > ",druga.a) 

    def __lt__(self, druga): 
        if(self.a<druga.a): 
            print(self.a, " < ",druga.a) 
        else: 
            print(self.a, " > ",druga.a) 



liczba1 = Liczba(4) 
liczba2 = Liczba(3) 

liczba1>=liczba2

liczba1>liczba2

liczba3 = Liczba(2) 
liczba4 = Liczba(3) 

liczba3<=liczba4

liczba3<liczba4






