class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

data1 = "abcd"
it = iter(data1)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

data2 = [1,2,4,6,3]
it2 = iter(data2)
print(it2)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
