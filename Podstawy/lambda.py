from math import pow

def function(f, liczba):
    return f(liczba)

print(function(lambda x: x * x, 4))

def kwadrat(x):
    return x * x

print(kwadrat(5))

wynik = (lambda x: x * x)(6) #argumenty tutaj
print(wynik)

lam = lambda x: x * x
print(lam(7))

lama = lambda x, y, z: (pow(x,z)/y)
print(lama(2,5,6))