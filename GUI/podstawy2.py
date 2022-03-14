from tkinter import *

def click():
    entered_text=textentry.get() #zbiera dane z okienka
    output.delete(0.0, END)
    try:
        definition = my_dick[entered_text]
    except:
        definition = "sorry ale nie ma tego"

    output.insert(END, definition)

def close_window():
    window.destroy()
    exit()

window = Tk()
window.title("DUPA PROGRAM")
window.resizable(False, False)
window.configure(background="black")

photo1=PhotoImage(file="yes.png") #idk ale musi byc png a nie jpg
Label (window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

Label (window, text = "Enter the word you would like a definition for: ", bg = "black", fg="white", font="none 12 bold").grid(row=1, column=0,sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0,sticky=W)

Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0,sticky=W)

Label (window, text = "\nDefinition: ", bg = "black", fg="white", font="none 12 bold").grid(row=4, column=0,sticky=W)

output=Text(window, width=40, height=3, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

my_dick={'algorithm': 'dupa po dupie az zrobi sie dupa', 'bug': 'blad w kodzie'}

Label (window, text = "click to exit: ", bg = "black", fg="white", font="none 12 bold").grid(row=6, column=0,sticky=W)

Button(window, text="EXIT", width=14, command=close_window).grid(row=7, column=0,sticky=W)

window.mainloop()