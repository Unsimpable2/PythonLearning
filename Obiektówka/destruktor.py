class Test:
    def __del__(self):
        print("Kuniec")

obj = Test()
obj2 = obj
lista = [obj2]

del obj
del obj2
del lista[0]

print("koniec")