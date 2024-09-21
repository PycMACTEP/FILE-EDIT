from tkinter import *
import os, sys, ctypes, shutil

win = Tk()
frame = Frame(win)

win2 = Tk()
frame2 = Frame(win2)

win.geometry("700x450")
win.resizable(width=False, height=False)
win.configure(background='black')
win.title("File Edit Launcher")
win.iconbitmap("sourse/lg.ico")

win2.geometry("300x200")
win2.resizable(width=False, height=False)
win2.configure(bg="black")
win2.title("MORE")
win2.iconbitmap("sourse/ml.ico")
win2.withdraw()

img = PhotoImage(file="sourse/logo.png")
ph = Label(win, image=img).pack(pady=5)

def open():
   os.startfile("data\\File edit.py")

def snowmore():
   win2.deiconify()

def btnback():
   win2.withdraw()

snmore = Button(win, text="MORE", command=snowmore)
btn = Button(win, text="OPEN FILE EDIT", command=open)

backbtn = Button(win2, text="X", command=btnback)

btn.pack(side=LEFT, pady=10, padx=10)
snmore.pack(side=RIGHT, pady=10, padx=10)

backbtn.pack(side=BOTTOM, padx=100, pady=10)

win.mainloop()
win2.mainloop()