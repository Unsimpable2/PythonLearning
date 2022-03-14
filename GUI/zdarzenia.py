import tkinter

root = tkinter.Tk()
root.geometry('480x480')

def Pisz1():
    print('dupa1')

def Pisz2(event): #do bind trzeba dac event
    print('dupa2 lewa')

def Pisz2Prawy(event):
    print('dupa2 prawa')

def Pisz3(event):
    print('dupa3')

def Okno(event):
    print('okno')

b1 = tkinter.Button(root, text = 'Przycisk 1', command = Pisz1)
b1.pack()

b2 = tkinter.Button(root, text = 'Przycisk 2')
b2.bind('<Button-1>', Pisz2)
b2.bind('<Button-3>', Pisz2Prawy)
b2.pack()

b3 = tkinter.Button(root, text = 'Przycisk 3')
b3.bind('<Button-3>', Pisz3)
b3.pack()

root.bind('<Button-2>', Okno)

root.mainloop()