import threading

def function1():
    for x in range(100):
        print("one")

def function2():
    for x in range(100):
        print("two")

t2 = threading.Thread(target=function1)
t3 = threading.Thread(target=function2)

t2.start()
t3.start()

t2.join()
t3.join()

print("YES!!!")