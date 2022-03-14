light =input("Jakie jest swiatlo? (red, green, yellow)\n")

if light =='red':
    print("czekaj")
elif light == 'yellow':
    print("przygotuj sie")
elif light == 'green':
    print("jedz")
else:
    print("niewlasciwa wartosc")

print("jedz!") if light == 'green' else print("czekaj!") #<--- dla dwoch opcji spoko ale dla wiekszej ilosci to nie

a = 5
b = 2

if a > b:
    print("a jest wieksze od b")
    print(f"{a} and {b}") #<--- inny sposób dodawania do ciagu wyswietlania