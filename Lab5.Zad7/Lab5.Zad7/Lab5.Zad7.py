class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        if(self.index % 2 == 0):
            pozycja = self.data[self.index]
            self.index+=2
            return pozycja
      


iterator = Parzyste([1,2,3,4,5])
#print(iterator)
for i in iterator:
    print(i)


