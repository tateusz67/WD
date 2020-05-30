def delSamo(tekst):
    wynik = tekst;
    samo = ('a', 'e', 'i', 'o', 'u','y','A', 'E', 'I', 'O', 'U','Y');
    for i in tekst:
        if i in samo:
            wynik = wynik.replace(i,"")
    return wynik


print(delSamo("Alabama"))