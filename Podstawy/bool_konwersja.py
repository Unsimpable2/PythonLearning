#3-------------

#rodzaje deklarowania stringa
name = "witek" #<---- jak chce np urzyć apostrofa w nazwie 
name = 'witek' #<---- tez git jak nie chcemy uzywac apostrofa
name = """wit

ek""" #<---- mozemy zawartos stringa na kilka linii i nie bedzie błedu(wyświetla w taki sposób jak zapisaliśmy)
print(name)

a = 10
b = 2.5
c=1_000_000 #<---- mozna tak zapisywac duze liczby by było bardziej czytelnie 

print(a+b)
print(c)

is_sky_blue=True
is_sun_blue=False

print(is_sky_blue)
print(is_sun_blue)

print(type(name))
print(type(a))
print(type(is_sky_blue))

first = 2 
second = "3"

print(first + int(second)) #<----by zmienic jakas zmienna na inny typ, trzeba dodac rodzaj zmiennej jaka chcemy i w nawiasie wpisac nazwe zmiennej
print(str(first) + second)

x=[1,2,3]
print(2 in x)
print(7 not in x) 