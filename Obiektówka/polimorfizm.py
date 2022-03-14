class Ksztalt:
    def __init__(self, nazwa="ksztalt"):
        self.nazwa = nazwa

    def pole(self):
        print(f'Brak danych na temat {self.nazwa}')

class Trojkat(Ksztalt):
    def __init__(self, nazwa = "Trojkat", a=2, h=2):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print(f'Pole figury {self.nazwa} to {self.a*self.h/2}')

class Prostokat(Ksztalt):
    def __init__(self, nazwa = "Prostokat", a=2, b=3):
        super().__init__(nazwa)
        self.a = a
        self.h = b

    def pole(self):
        print(f'Pole figury {self.nazwa} to {self.a*self.h}')

class Kwadrat():
    def __init__(self, nazwa = "kwadrat", a=2):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print(f'Pole figury {self.nazwa} to {self.a**2}')

def wyswietlPole(lista):
    for x in lista:
        x.pole()

kasztalt = Ksztalt()
trojkat = Trojkat()
prostokat = Prostokat()
kwadrat = Kwadrat()

lista = [kasztalt, trojkat, prostokat, kwadrat]
wyswietlPole(lista)