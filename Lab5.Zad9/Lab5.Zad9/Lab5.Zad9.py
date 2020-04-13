def samogloski(wyraz,smgloski):
        wynik = [each for each in wyraz if each in smgloski] 
        yield wynik 


gen = samogloski("testowy", "AaEeIiOoUuYy")
print(next(gen))

gen2 = samogloski("samogloska", "AaEeIiOoUuYy")
print(next(gen2))
