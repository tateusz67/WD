def fibonacci(n):
    a=0 
    b=1
    for i in range(n):
        yield a
        b+=a
        a=b-a

print(list(fibonacci(15)))
