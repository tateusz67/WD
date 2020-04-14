miesiace = ["Styczen","Luty","Marzec","Kwiecien","Maj","Czerwiec","Lipiec","Sierpien","Wrzesien","Pazdziernik","Listopad","Grudzien"]

miesiac = (miesiac for miesiac in miesiace)
print(miesiac)
for i in range(12):
    print(next(miesiac))

