name = "witek"
name2= "[ULA];"
name3= "duuupad"
name4="            ziobro         "

print(len(name))
print(name.capitalize())
print(name.upper())
print(name2.lower())
print(name[0])
print(name[0:2])
print(name[3:])
print(name[-3:]) #<--- od konca
channel="witek ty kurwo jebana przestan mi rodzine przesladowac"
print(channel.split(" "))

join_string = " "
print(join_string.join(['dupa', 'jedna', 'nie', 'ruchana']))

print(name.startswith("W"))
print(name.startswith("w"))

print(name.endswith("K"))
print(name.endswith("k"))

print(name2.rstrip("];")) #<---- prawa strona
print(name2.lstrip("[")) #<---- lewa strona
print(name3.strip("d")) #<--- z lewej i prawej strony
print(name4.strip()) #<---- usuwa spacje

print(name + " " + name2)
print(join_string.join([name, name2]))

james_bond=7

print(str(james_bond).zfill(3))