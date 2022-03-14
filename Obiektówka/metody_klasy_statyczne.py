class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print(f"Nazywam sie {self.imie}")

    @classmethod
    def nowy_czlek(cls, imie):
        return cls(imie)

    @staticmethod
    def przywitaj(arg):
        print(f"Czesc {arg}")


cz1 = Czlowiek.nowy_czlek("Dawid")
cz1.przedstaw()
cz2 = cz1.nowy_czlek("Seba")
cz2.przedstaw()

Czlowiek.przywitaj("ziom!")