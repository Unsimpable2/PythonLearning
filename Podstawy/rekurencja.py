def function(x):
    return x * x

zmienna = function
print(zmienna(5))

def func(f1, x): #mozna jako argument posłać inna funkcje
    return f1(x) * x

print(func(function, 5))

#rekurencja

def silnia(x):
        if x <= 1:
            return 1
        else:
            return x * silnia(x - 1)
        
print(silnia(6))