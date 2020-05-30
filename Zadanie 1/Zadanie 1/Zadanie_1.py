def odwroc(a): 
    rozdziel = a.split(' ') 
    temp = [slowo[::-1] for slowo in rozdziel] 
    wynik = " ".join(temp) 
  
    return wynik 
  
zdanie = "Ala ma kota"
print(odwroc(zdanie))


