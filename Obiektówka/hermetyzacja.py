class Test:
    __lista = [] #prywatna _lista lub __lista

    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return 

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj._Test__lista.append("X") #jak jest __ to trzeba dodac jeszcze nazwe klasy z jednym _
print(obj.zdejmij())