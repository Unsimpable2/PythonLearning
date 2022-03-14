number1 = 1
number = 1

while number < 6:
    print(number)
    number+=1

print("\n")

for number1 in range(0, 10): #<----- od jakiejs do jakiejs i o ile
    if number1 == 5:
        break #continue ominie dana wartosc warunku i pójdzie dalej
    print(number1)