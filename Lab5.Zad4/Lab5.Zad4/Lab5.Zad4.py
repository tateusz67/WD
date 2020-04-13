class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
#print(p1.counter)
#print(p2.counter)
#p1.update(1)
#print(p1.counter)
#print(p2.counter)

p3 = Point(6,1)
p4 = Point(-2,8)
p5 = Point(-6,-6)

print(p3.counter)
p3.update(1)
print(p4.counter)
p3.update(5)
p4.update(-2)
print(p5.counter)


