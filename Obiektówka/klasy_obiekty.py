class Czlowiek:

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstawSie(self, powitanie = "Czesc"): #self pozwala sie odwoływac do zmiennych w całej klasie
        return (f"{powitanie} jestem {self.imie}, mam {self.wiek}, chcesz wpr synek?")

obiekt = Czlowiek("Seba", 20)
obiekt2 = Czlowiek("Dawid", 18)

print(obiekt.przedstawSie("ELO MORDO"))
print(obiekt2.przedstawSie())