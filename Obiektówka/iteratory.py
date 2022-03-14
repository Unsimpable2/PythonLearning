lista = [1,2,4]

iteratorLista=iter(lista)
print(iteratorLista)
print(next(iteratorLista))
print(next(iteratorLista))
print(next(iteratorLista))

class IteratorM():
    def __init__(self, maks=40):
        self.x = 1
        self.max = maks

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x

        if x > self.max:
            raise StopIteration

        self.x +=5
        return x

for i in IteratorM():
    print(i)

class Odwroc():
    def __init__(self, dane="kamilslimak"):
        self.dane = dane
        self.indeks= len(dane)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks == 0:
            raise StopIteration

        self.indeks -=1
        return self.dane[self.indeks]

for i in Odwroc():
    print(i, end='')