c_info={}
c_info["Poland"]=("Waszawa", 37.97)
c_info["Germany"]=("Berlin", 83.02)
c_info["Slowacja"]=("Bratyslawa", 5.45)

def show_info(country):
    print(country+"\n")
    print("Stolica: " + county_info[0])
    print("Liczba mieszkancow w mil: " + str(county_info[1]))

for country in c_info.keys():
    print(country)

country = input("O jakim kraju chcesz wyswietlic? \n")
county_info=c_info.get(country)
show_info(country)

#--------------------------------

def dodaj(x):
    print(f"{x + 1}\n")

def odejmij(x, y):
    print(f"{x - y}\n")

def mnoz(x, y = 2): #y to parametr domyslny
    print(f"{x * y}\n")

def dziel(x, y, z):
    return x/y/z

dodaj(2)
odejmij(2, 5)
mnoz(2)
print(dziel(4, 6, 3))
#ta sama nazwa funkcji = nadpisanie jej pozniejsza