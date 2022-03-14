import math

class Punk2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(pow(x,2)+pow(y,2))

    def __add__(self, drugi):
        return Punk2D(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):
        return self.odleglosc  < drugi.odleglosc

    def __eq__(self, drugi):
        return self.x==drugi.x and self.y==drugi.y

    def __len__(self):
        return int(round(self.odleglosc,0))


p1 = Punk2D(2,5)
p2 = Punk2D(3,6)
p3 = p1 + p2

print(p3.odleglosc)
print(p1 < p2)
print(p1 > p2)
print(p1.odleglosc)
print(p2.odleglosc)
print(p1 == p2)
print(p2 == p2)
print(len(p3))