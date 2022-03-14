import tkinter as OpenApps
from tkinter import filedialog
import os

root = OpenApps.Tk()
root.resizable(False, False)
root.title("Open Apps")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps= tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe" ), ("all files", "*.*")))

    apps.append(filename)
    print(filename)

    for app in apps:
        label = OpenApps.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delApps():
    apps.clear()

canvas = OpenApps.Canvas(root, height=700, width=700, bg="#4251D1")
canvas.pack()

frame = OpenApps.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = OpenApps.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#4251D1", command=addApp)
run = OpenApps.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#4251D1", command=runApps)
delete = OpenApps.Button(root, text="Delete", padx=10, pady=5, fg="white", bg="#4251D1", command=delApps)

openFile.pack(side=OpenApps.LEFT, fill=OpenApps.BOTH, expand=True)
run.pack(side=OpenApps.LEFT, fill=OpenApps.BOTH, expand=True)
delete.pack(side=OpenApps.LEFT, fill=OpenApps.BOTH, expand=True)

for app in apps:
    label = OpenApps.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')