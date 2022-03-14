#5--------------
a=5
b=5

print(a==5) #<--- zwraca boola
print(a!=5)
print(a>5)
print(a<5)

print(a<=5)
print(a>=5)

print(a==b)

print(a is b) #<---- "is" nie porównuje wartosci a adresy w pamieci

x= 10
if type(x) is int:
    print("x is int")
else:
    print("x is not int")

y= "hello"
if type(y) is int:
    print("x is int")
else:
    print("x is not int")