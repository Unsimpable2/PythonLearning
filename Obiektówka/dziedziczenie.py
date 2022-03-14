class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doggo(Animal): #dziedziczenie
    def voice(self):
        print("BORK BORK")

class Wolf(Doggo):
    def getVoice(self):
        print("I am Wolf!")
        super().voice()

class Kitku(Animal):
    def getVoice(self):
        print("Mial Mial Nigga")

Dog = Doggo("Galgan", 6)
Cat = Kitku("Czarny", 4)
wolf= Wolf("Gerwant", 55)

print(Dog.name)
print(Dog.age)
Dog.voice()

print(Cat.name)
print(Cat.age)
Cat.getVoice()

print(wolf.name)
print(wolf.age)
wolf.getVoice()