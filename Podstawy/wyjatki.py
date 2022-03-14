countriec_and_capitals={'Poland':'Warsaw','Germany':'Berlin', 'Czechia':'Prague'}

try:
    print(2/0)
    print(countriec_and_capitals['USA'])

except KeyError:  #<--------- jak wiemy jaki bład moze byc to wtedy uzywamy typu błedu
    print("Klucz nie zostal znaleziony")

except ZeroDivisionError:
    print("Nie mozna dzielic przez 0")

finally:
    print("To wykona sie zawsze")

print("Jestem tutaj")

#--------------------------------------

def dzielenie(x, y):
    assert y !=0, "Y == 0"
    #if y == 0:
        #raise ZeroDivisionError("Dzielenie przez 0")
    print(x/y)

try:
    dzielenie(1,1)

except ZeroDivisionError:
    print("Blad!")
    raise


