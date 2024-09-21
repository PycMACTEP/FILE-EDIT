from tkinter import *
from tkinter import filedialog
import os, sys, io

window = Tk()
frame = Frame(window)
window.resizable(width=False, height=False)
window.geometry("300x200")
window.title("Select a file")
window.iconbitmap("sourse/nico.ico")
window.configure(background="black")

def close():
    sys.exit(1)

newfilename = ""

global filename
filename = ""

def edit_txt():
    os.startfile("data\\te.py")

def edit_photo():
    os.startfile("data\\photo.py")

def video_edit():
    os.startfile("data\\videoedit.py")

def choise():
    labb = Label(window, text="The program cannot read this file", bg="Black", fg="White")
    klab = Label(window, text="Its a python file:)", bg="Black", fg="White")
    def ret():
        window.geometry("300x200")
        labb.pack_forget()
        lb.pack_forget()
        openb.pack_forget()
        btn.pack(pady=5)
        res.pack_forget()
        exit.pack_forget()
        exit.pack(pady=5)
        bt_n.pack_forget()
        klab.pack_forget()
        return choise
    window.title("Selecting a file")
    filename = filedialog.askopenfile()
    if filename == None:
        return choise
    window.geometry("500x200")
    window.title("Editing a file")
    filename_str = filename.name
    repsourse = " mode='r' encoding='cp1251'"
    newfilename = filename_str.replace(repsourse, "")
    with io.open("sourse/selectedfile.txt", "w+", encoding="utf-8") as file:
        pass
        content = file.read()
        file.seek(0)
        file.write(newfilename)
        file.close()
    type_file = newfilename[-4:]
    print(type_file)
    def open():
        os.startfile(newfilename)
    bt_n = Button(window, text="Edit a file")
    if type_file == ".txt" or type_file == ".rtf":
        bt_n.pack(pady=5)
        bt_n.config(command=edit_txt)
    elif type_file ==".png" or type_file == ".jpg" or type_file == "jpeg" or type_file == "webp" or type_file == ".bmp" or type_file == ".gif":
        bt_n.config(command=edit_photo)
        bt_n.pack(pady=5)
    elif type_file[-3:] == ".py":
        klab.pack(pady=5)
    elif type_file == ".mp4" or type_file == ".AVI":
        bt_n.config(command=video_edit)
        bt_n.pack(pady=5)
    else:
        labb.pack(pady=5)
    lb = Label(window, text="Your file is \n" + str(newfilename), bg="Black", fg="White") 
    openb = Button(window, text="Open the selected file", command=open)
    res = Button(window, text="Reselect", command=ret)
    lb.pack(pady=5)
    openb.pack(pady=5)
    btn.pack_forget()
    res.pack(pady=5)
    exit.pack_forget()
    exit.pack(pady=5)

exit = Button(window, text="Close", width=5, height=1, command=close) 
btn = Button(window, text="Select file", width=20, height=1, command=choise)

btn.pack(pady=5)
exit.pack()

window.mainloop()