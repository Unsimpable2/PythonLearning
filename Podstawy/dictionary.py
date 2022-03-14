countriec_and_capitals={"Poland":"Warsaw","Germany":"Berlin"}
print(countriec_and_capitals)

countriec_and_capitals['Czechia']= "Prague"
print(countriec_and_capitals)

for k in countriec_and_capitals.keys():
    print(k)

for v in countriec_and_capitals.values():
    print(v)

for k, v in countriec_and_capitals.items():
    print(f"{k} and {v}")

print(countriec_and_capitals["Poland"]) #<----- jak nie bedzie Poland to bedzie bład
print(countriec_and_capitals.get("Poland")) #<----- jak nie bedzie Poland to wyswietli none

print(countriec_and_capitals.setdefault("USA","Washington DC")) #<--------- jak nie ma to doda do słownika
print(countriec_and_capitals)

if "Poland" in countriec_and_capitals.keys():
    print("Znaleziono")
else:
    print("Nieznaleziono")

countriec_and_capitals.clear()
print(countriec_and_capitals)

person = {'name': 'Mark'}
print(person)
person['newkey'] = 67 
print(person)