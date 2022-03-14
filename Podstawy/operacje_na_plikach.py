file = open("operacje_na_plikach", "w+")

countriec_and_capitals={'Poland':'Warsaw','Germany':'Berlin', 'Czechia':'Prague'}

for country, capitals in countriec_and_capitals.items():
    file.write(country + " - " + capitals + "\n")

file.close()

file = open("file.txt")

for line in file.readlines():
    print(line.strip())

file.close()