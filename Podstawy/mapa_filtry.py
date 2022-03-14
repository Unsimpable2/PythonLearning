liczba = [2, 10, 12, 15, 20, 25, 30, 35]
liczba2 = [5, 3460, 242, 15, 204, 2475, 3480, 385]

#mapa

def funkcja(x):
    return x * x

wynik = map(funkcja, liczba)
print(list(wynik))

wynik2 = map(lambda x: x*x, liczba2)
print(list(wynik2))

#filtry

wynik3 = filter(lambda x: x % 2 == 0, liczba2) #zawsze 1 argument, wynik w postaci T/F
print(list(wynik3))