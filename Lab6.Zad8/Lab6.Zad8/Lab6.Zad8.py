import numpy as np

def funkcja(x,kierunek):

    if(np.size(x) %2 != 0):
        print("Nie mozna podzielic tej macierzy")
        exit()
    if(kierunek == 'x'):
        print(np.vsplit(x, 2))
    if(kierunek == 'y'):
        print(np.hsplit(x, 2))



x = np.arange(36).reshape(6,6)
print(x,'\n')

funkcja(x,'x')




