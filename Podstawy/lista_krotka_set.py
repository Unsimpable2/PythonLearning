names_list=[]
names_list.append("Witek")
names_list.append("Masal")
names_list.append("Masal")

print(names_list)

names_list.reverse()

print(names_list)

name = ["witek", "masal"]
print(name)

for i in name:
    print(i)

names_list.append("Ula")
name.sort()
print(name)
name.sort(reverse=True)
print(name)

print(names_list)
print(names_list[0])

print(names_list.count("Masal"))
print(len(names_list))

print(names_list.pop(0))
print(names_list)

names_list.remove("Witek") #musi byc w liscie
print(names_list)

names_list2=["Dominik"]

names_list3=names_list+names_list2
print(names_list3)

mylist=[10, 20, 30, "string", True, 8.97]
mylist2=[10, 20, 30, 8.97]

print(mylist[:3])
print(mylist[1:3])
print(mylist[-2]) #z prawej do lewej
mylist[3] = "another string"
print(mylist)

for x in mylist:
    print(x)

for x in mylist2:
    print(2 ** x)

x=[1,2,3]
y=[4,5,6]
z=[64,35,1,673,341,12]
print(x+y)

print(len(x))
print(max(y)) #nie z stringami i bool
print(min(y)) #nie z stringami i bool

x.insert(2, 43)
print(x)

print(x.index(1))
print(sorted(z))

#---------------- Krotka
ludzie=("Witek", "Ula", "Ciapek", "Puciek")
print(ludzie) #<-------- struktura niezmienna, nic sie nie da zmienic
print(ludzie.count("Witek"))

x=(1,2,3) #dodanie do krotki
x=list(x)
x[3]=10
x= tuple(x)
print(x)

#---------------- Set
names_set= {"Witek", "Ula", "Ciapek", "Witek"}
print(names_set) #<---- kasuje duplikacje
name_set=set() #<---- pusty set, mozna dodac cos za pomoca add
names_set.remove("Witek") #<---- a jak nie ma to bedzie błąd
names_set.discard("Ciapek") #<---- jak nie ma to sie nic nie wydarzy

for name in names_set:
    print(name)

names_set1= {"Witek", "Ula"}
names_set2= {"Ciapek"}

names_set3= names_set1.union(names_set2)
for name in names_set3:
    print(name)

name_set4={"maja", "ada", "lukasz"}
name_set5={"maja","dominik","adam"}
name_set6=name_set4.difference(name_set5) #<--- róznica

for name in name_set6:
    print(name)

name_set6=name_set4.intersection(name_set5) #<--- czesc wspólna

for name in name_set6:
    print(name)

name_set6=name_set4.symmetric_difference(name_set5) #<--- elementy spoza czesci wpsolnej

for name in name_set6:
    print(name)

namesss=["karol"]
nameset={"marcin"}

namesss.extend(nameset)
print(namesss)