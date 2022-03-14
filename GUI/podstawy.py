import tkinter

root = tkinter.Tk()
root.geometry('480x480')

l = tkinter.Label(root, text = 'Aplikacja')
l.pack()

def funkcjaP():
    print('wcisnieto knefla')

b = tkinter.Button(root, text = 'Jestem przyciskiem1', width = 10, bg = "red", fg = "white" ,command = funkcjaP)
b.pack(side = tkinter.RIGHT)

b2 = tkinter.Button(root, text = 'Jestem przyciskiem2', command = funkcjaP)
b2.place(x = 350, y = 0)

root.mainloop()