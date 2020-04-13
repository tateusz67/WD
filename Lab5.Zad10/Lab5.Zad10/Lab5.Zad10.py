import itertools

a=[1,2,3,4,5,6,7,8,9,10]

itertools.permutations(a,3)
for i in itertools.permutations(a,3):
    print(i)