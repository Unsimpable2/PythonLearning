def switch():
    x=input()
    match x:
        case "1":
            print("Ziobro")
            switch()
            
        case "2":
            print("Ty")
            switch()
            
        case "3":
            print("Kurwo")
            switch()
            
        case "4":
            print("Jebana")
            switch()

        case _:
            print("No chyba nie")
            exit()

switch()