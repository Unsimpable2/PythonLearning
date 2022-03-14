import datetime

imie = "witek"
wiek = 22

def printtext():
    return "!!!"

zdanie =f"{printtext()} czesc, mam na imie {imie} i mam {wiek} lat"
zdanie2 =f"czesc, mam na imie {imie.upper()} i mam {wiek} lat"
print(zdanie)
print(zdanie2)

number = 2
print(f'{number * 2}')

number2 = 21.5
print(f'{number2:.5f}')

number3 = 1234567
print(f'{number3:,}')

number4 = 300
print(f'{number4:b}') #o - ósemkowy x/X - hexa

number5 = 64
print(f'{number5:c}') #ascii

now = datetime.datetime.now()
print(now)
print(f'{now:%Y-%m-%d %H:%M}')

names_and_sal={'Kamil':15000, 'Mariusz': 20000, 'Dominik': 5000, 'Bardzo Dlugie Imie': 6000}

for name, salary in names_and_sal.items():
    print(f'{name:30} {salary}')

print(f'{imie:>10}')
print(f'{wiek:>5}')

print(f'{imie=}')
print(f'{wiek=}')

output =f"""{imie}
    {wiek}

hello
"""

print(output)