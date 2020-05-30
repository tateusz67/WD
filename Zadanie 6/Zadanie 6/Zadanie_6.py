def fibonacci(n):
    if n<0:
        return 0
    if n==1 or n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)


fibo = []
n = int(input("Podaj dlugosc ciagu: "))
for i in range(1,n+1):
    fibo.append(fibonacci(i))

print(fibo)
