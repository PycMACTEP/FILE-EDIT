from tkinter import *
from tkinter import messagebox as ms
import PIL, io, sys, os
from PIL import Image, ImageDraw, ImageTk
import PIL.Image
from random import *

win = Tk()
mmenu = Menu(win)

win.iconbitmap("sourse/nico.ico")
win.geometry("800x700")
win.config(bg="white")
win.title("Editing a photo")
win.resizable(width=False, height=False)

win2 = Tk()

win2.config(bg="Black")
win2.resizable(width=False, height=False)
win2.geometry("300x500")
win2.title("Plugin Manager")
win2.iconbitmap("sourse/veicon.ico")
win2.withdraw()

can = Canvas(win2)
can.pack(side="bottom", fill="both", expand=1)

v = Scrollbar(can, orient="vertical", command=can.yview, border=0)
v.pack(side = RIGHT, fill="y")

can.config(yscrollcommand=v.set)

frame = Frame(can, bg="black", border=0)
can.create_window((0,0), window=frame, anchor="nw")
can.bind("<Configure>", lambda e: can.config(scrollregion = can.bbox("all")))

can.config(yscrollcommand=v.set, bg="black", border=0)
can.yview_moveto(0)

def cl():
    win2.withdraw()

x = Button(frame, text="X", command=cl, pady=2, padx=3).pack(side=RIGHT, padx=5)

pathname = os.path.dirname(sys.argv[0])
plugpath = pathname[:-5]
plugpath = plugpath + "/plugins for photo edit"
pathname = pathname[:-5]

if len(os.listdir(plugpath)) == 0:
    pass
else:
    pass

plugin1 = plugpath + "/plugin1"
plugin2 = plugpath + "/plugin2"
plugin3 = plugpath + "/plugin3"
plugin4 = plugpath + "/plugin4"
plugin5 = plugpath + "/plugin5"
plugin6 = plugpath + "/plugin6"
plugin7 = plugpath + "/plugin7"
plugin8 = plugpath + "/plugin8"
plugin9 = plugpath + "/plugin9"
plugin10 = plugpath + "/plugin10"
plugin11 = plugpath + "/plugin11"
plugin12 = plugpath + "/plugin12"
plugin13 = plugpath + "/plugin13"
plugin14 = plugpath + "/plugin14"
plugin15 = plugpath + "/plugin15"
plugin16 = plugpath + "/plugin16"
plugin17 = plugpath + "/plugin17"
plugin18 = plugpath + "/plugin18"
plugin19 = plugpath + "/plugin19"
plugin20 = plugpath + "/plugin20"
plugin21 = plugpath + "/plugin21"
plugin22 = plugpath + "/plugin22"
plugin23 = plugpath + "/plugin23"
plugin24 = plugpath + "/plugin24"
plugin25 = plugpath + "/plugin25"
plugin26 = plugpath + "/plugin26"
plugin27 = plugpath + "/plugin27"
plugin28 = plugpath + "/plugin28"
plugin29 = plugpath + "/plugin29"
plugin30 = plugpath + "/plugin30"
plugin31 = plugpath + "/plugin31"
plugin32 = plugpath + "/plugin32"

def o1():
    os.startfile(plugin1 + "/main.exe")

def o2():
    os.startfile(plugin2 + "/main.exe")

def o3():
    os.startfile(plugin3 + "/main.exe")

def o4():
    os.startfile(plugin4 + "/main.exe")

def o5():
    os.startfile(plugin5 + "/main.exe")

def o6():
    os.startfile(plugin6 + "/main.exe")

def o7():
    os.startfile(plugin7 + "/main.exe")

def o8():
    os.startfile(plugin8 + "/main.exe")

def o9():
    os.startfile(plugin9 + "/main.exe")

def o10():
    os.startfile(plugin10 + "/main.exe")

def o11():
    os.startfile(plugin11 + "/main.exe")

def o12():
    os.startfile(plugin12 + "/main.exe")

def o13():
    os.startfile(plugin13 + "/main.exe")

def o14():
    os.startfile(plugin14 + "/main.exe")

def o15():
    os.startfile(plugin15 + "/main.exe")

def o16():
    os.startfile(plugin16 + "/main.exe")

def o17():
    os.startfile(plugin17 + "/main.exe")

def o18():
    os.startfile(plugin18 + "/main.exe")

def o19():
    os.startfile(plugin19 + "/main.exe")

def o20():
    os.startfile(plugin20 + "/main.exe")

def o21():
    os.startfile(plugin21 + "/main.exe")

def o22():
    os.startfile(plugin22 + "/main.exe")

def o23():
    os.startfile(plugin23 + "/main.exe")

def o24():
    os.startfile(plugin24 + "/main.exe")

def o25():
    os.startfile(plugin25 + "/main.exe")

def o26():
    os.startfile(plugin26 + "/main.exe")

def o27():
    os.startfile(plugin27 + "/main.exe")

def o28():
    os.startfile(plugin28 + "/main.exe")

def o29():
    os.startfile(plugin29 + "/main.exe")

def o30():
    os.startfile(plugin30 + "/main.exe")

def o31():
    os.startfile(plugin31 + "/main.exe")

def o32():
    os.startfile(plugin32 + "/main.exe")

error1 = 0
error2 = 0
error3 = 0
error4 = 0
error5 = 0
error6 = 0
error7 = 0
error8 = 0
error9 = 0
error10 = 0
error11 = 0
error12 = 0
error13 = 0
error14 = 0
error15 = 0
error16 = 0
error17 = 0
error18 = 0
error19 = 0
error20 = 0
error21 = 0
error22 = 0
error23 = 0
error24 = 0
error25 = 0
error26 = 0
error27 = 0
error28 = 0
error29 = 0
error30 = 0
error31 = 0
error32 = 0

try:
    with open(plugin1 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name1 = plug.read()
        plug.close()
    with open(plugin1 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie1 = plug.read()
        plug.close()
except FileNotFoundError:
    error1 = 1

try:
    with open(plugin2 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name2 = plug.read()
        plug.close()
    with open(plugin2 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie2 = plug.read()
        plug.close()
except FileNotFoundError:
    error2 = 1

try:
    with open(plugin3 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name3 = plug.read()
        plug.close()
    with open(plugin3 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie3 = plug.read()
        plug.close()
except FileNotFoundError:
    error3 = 1

try:
    with open(plugin4 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name4 = plug.read()
        plug.close()
    with open(plugin4 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie4 = plug.read()
        plug.close()
except FileNotFoundError:
    error4 = 1

try:
    with open(plugin5 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name5 = plug.read()
        plug.close()
    with open(plugin5 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie5 = plug.read()
        plug.close()
except FileNotFoundError:
    error5 = 1

try:
    with open(plugin6 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name6 = plug.read()
        plug.close()
    with open(plugin6 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie6 = plug.read()
        plug.close()
except FileNotFoundError:
    error6 = 1

try:
    with open(plugin7 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name7 = plug.read()
        plug.close()
    with open(plugin7 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie7 = plug.read()
        plug.close()
except FileNotFoundError:
    error7 = 1

try:
    with open(plugin8 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name8 = plug.read()
        plug.close()
    with open(plugin8 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie8 = plug.read()
        plug.close()
except FileNotFoundError:
    error8 = 1

try:
    with open(plugin9 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name9 = plug.read()
        plug.close()
    with open(plugin9 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie9 = plug.read()
        plug.close()
except FileNotFoundError:
    error9 = 1

try:
    with open(plugin10 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name10 = plug.read()
        plug.close()
    with open(plugin10 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie10 = plug.read()
        plug.close()
except FileNotFoundError:
    error10 = 1

try:
    with open(plugin11 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name11 = plug.read()
        plug.close()
    with open(plugin11 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie11 = plug.read()
        plug.close()
except FileNotFoundError:
    error11 = 1

try:
    with open(plugin12 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name12 = plug.read()
        plug.close()
    with open(plugin12 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie12 = plug.read()
        plug.close()
except FileNotFoundError:
    error12 = 1

try:
    with open(plugin13 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name13 = plug.read()
        plug.close()
    with open(plugin13 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie13 = plug.read()
        plug.close()
except FileNotFoundError:
    error13 = 1

try:
    with open(plugin14 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name14 = plug.read()
        plug.close()
    with open(plugin14 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie14 = plug.read()
        plug.close()
except FileNotFoundError:
    error14 = 1

try:
    with open(plugin15 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name15 = plug.read()
        plug.close()
    with open(plugin15 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie15 = plug.read()
        plug.close()
except FileNotFoundError:
    error15 = 1

try:
    with open(plugin16 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name16 = plug.read()
        plug.close()
    with open(plugin16 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie16 = plug.read()
        plug.close()
except FileNotFoundError:
    error16 = 1

try:
    with open(plugin17 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name17 = plug.read()
        plug.close()
    with open(plugin17 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie17 = plug.read()
        plug.close()
except FileNotFoundError:
    error17 = 1

try:
    with open(plugin18 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name18 = plug.read()
        plug.close()
    with open(plugin18 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie18 = plug.read()
        plug.close()
except FileNotFoundError:
    error18 = 1

try:
    with open(plugin19 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name19 = plug.read()
        plug.close()
    with open(plugin19 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie19 = plug.read()
        plug.close()
except FileNotFoundError:
    error19 = 1

try:
    with open(plugin20 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name20 = plug.read()
        plug.close()
    with open(plugin20 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie20 = plug.read()
        plug.close()
except FileNotFoundError:
    error20 = 1

try:
    with open(plugin21 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name21 = plug.read()
        plug.close()
    with open(plugin21 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie21 = plug.read()
        plug.close()
except FileNotFoundError:
    error21 = 1

try:
    with open(plugin22 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name22 = plug.read()
        plug.close()
    with open(plugin22 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie22 = plug.read()
        plug.close()
except FileNotFoundError:
    error22 = 1

try:
    with open(plugin23 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name23 = plug.read()
        plug.close()
    with open(plugin23 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie23 = plug.read()
        plug.close()
except FileNotFoundError:
    error23 = 1

try:
    with open(plugin24 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name24 = plug.read()
        plug.close()
    with open(plugin24 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie24 = plug.read()
        plug.close()
except FileNotFoundError:
    error24 = 1

try:
    with open(plugin25 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name25 = plug.read()
        plug.close()
    with open(plugin25 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie25 = plug.read()
        plug.close()
except FileNotFoundError:
    error25 = 1

try:
    with open(plugin26 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name26 = plug.read()
        plug.close()
    with open(plugin26 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie26 = plug.read()
        plug.close()
except FileNotFoundError:
    error26 = 1

try:
    with open(plugin27 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name27 = plug.read()
        plug.close()
    with open(plugin27 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie27 = plug.read()
        plug.close()
except FileNotFoundError:
    error27 = 1

try:
    with open(plugin28 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name28 = plug.read()
        plug.close()
    with open(plugin28 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie28 = plug.read()
        plug.close()
except FileNotFoundError:
    error28 = 1

try:
    with open(plugin29 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name29 = plug.read()
        plug.close()
    with open(plugin29 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie29 = plug.read()
        plug.close()
except FileNotFoundError:
    error29 = 1

try:
    with open(plugin30 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name30 = plug.read()
        plug.close()
    with open(plugin30 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie30 = plug.read()
        plug.close()
except FileNotFoundError:
    error30 = 1

try:
    with open(plugin31 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name31 = plug.read()
        plug.close()
    with open(plugin31 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie31 = plug.read()
        plug.close()
except FileNotFoundError:
    error31 = 1

try:
    with open(plugin32 + "/Config/Name.txt", "r", encoding="utf-8") as plug:
        name32 = plug.read()
        plug.close()
    with open(plugin32 + "/Config/Opisanie.txt", "r", encoding="utf-8") as plug:
        opisanie32 = plug.read()
        plug.close()
except FileNotFoundError:
    error32 = 1

def vvim():
    win2.deiconify()

if error1 == 0:
    l1 = Label(frame, text=name1, bg="black", fg="white").pack()
    b1 = Label(frame, text=opisanie1, bg="black", fg="white").pack()
    bb1 = Button(frame, text="Start Plugin", command=o1).pack()
else:
    pass

if error2 == 0:
    l2 = Label(frame, text=name2, bg="black", fg="white").pack()
    b2 = Label(frame, text=opisanie2, bg="black", fg="white").pack()
    bb2 = Button(frame, text="Start Plugin", command=o2).pack()
else:
    pass

if error3 == 0:
    l3 = Label(frame, text=name3, bg="black", fg="white").pack()
    b3 = Label(frame, text=opisanie3, bg="black", fg="white").pack()
    bb3 = Button(frame, text="Start Plugin", command=o3).pack()
else:
    pass

if error4 == 0:
    l4 = Label(frame, text=name4, bg="black", fg="white").pack()
    b4 = Label(frame, text=opisanie4, bg="black", fg="white").pack()
    bb4 = Button(frame, text="Start Plugin", command=o4).pack()
else:
    pass

if error5 == 0:
    l5 = Label(frame, text=name5, bg="black", fg="white").pack()
    b5 = Label(frame, text=opisanie5, bg="black", fg="white").pack()
    bb5 = Button(frame, text="Start Plugin", command=o5).pack()
else:
    pass

if error6 == 0:
    l6 = Label(frame, text=name6, bg="black", fg="white").pack()
    b6 = Label(frame, text=opisanie6, bg="black", fg="white").pack()
    bb6 = Button(frame, text="Start Plugin", command=o6).pack()
else:
    pass

if error7 == 0:
    l7 = Label(frame, text=name7, bg="black", fg="white").pack()
    b7 = Label(frame, text=opisanie7, bg="black", fg="white").pack()
    bb7 = Button(frame, text="Start Plugin", command=o7).pack()
else:
    pass

if error8 == 0:
    l8 = Label(frame, text=name8, bg="black", fg="white").pack()
    b8 = Label(frame, text=opisanie8, bg="black", fg="white").pack()
    bb8 = Button(frame, text="Start Plugin", command=o8).pack()
else:
    pass

if error9 == 0:
    l9 = Label(frame, text=name9, bg="black", fg="white").pack()
    b9 = Label(frame, text=opisanie9, bg="black", fg="white").pack()
    bb9 = Button(frame, text="Start Plugin", command=o9).pack()
else:
    pass

if error10 == 0:
    l10 = Label(frame, text=name10, bg="black", fg="white").pack()
    b10 = Label(frame, text=opisanie10, bg="black", fg="white").pack()
    bb10 = Button(frame, text="Start Plugin", command=o10).pack()
else:
    pass

if error11 == 0:
    l11 = Label(frame, text=name11, bg="black", fg="white").pack()
    b11 = Label(frame, text=opisanie11, bg="black", fg="white").pack()
    bb11 = Button(frame, text="Start Plugin", command=o11).pack()
else:
    pass

if error12 == 0:
    l12 = Label(frame, text=name12, bg="black", fg="white").pack()
    b12 = Label(frame, text=opisanie12, bg="black", fg="white").pack()
    bb12 = Button(frame, text="Start Plugin", command=o12).pack()
else:
    pass

if error13 == 0:
    l13 = Label(frame, text=name13, bg="black", fg="white").pack()
    b13 = Label(frame, text=opisanie13, bg="black", fg="white").pack()
    bb13 = Button(frame, text="Start Plugin", command=o13).pack()
else:
    pass

if error14 == 0:
    l14 = Label(frame, text=name14, bg="black", fg="white").pack()
    b14 = Label(frame, text=opisanie14, bg="black", fg="white").pack()
    bb14 = Button(frame, text="Start Plugin", command=o14).pack()
else:
    pass

if error15 == 0:
    l15 = Label(frame, text=name15, bg="black", fg="white").pack()
    b15 = Label(frame, text=opisanie15, bg="black", fg="white").pack()
    bb15 = Button(frame, text="Start Plugin", command=o15).pack()
else:
    pass

if error16 == 0:
    l16 = Label(frame, text=name16, bg="black", fg="white").pack()
    b16 = Label(frame, text=opisanie16, bg="black", fg="white").pack()
    bb16 = Button(frame, text="Start Plugin", command=o16).pack()
else:
    pass

if error17 == 0:
    l17 = Label(frame, text=name17, bg="black", fg="white").pack()
    b17 = Label(frame, text=opisanie17, bg="black", fg="white").pack()
    bb17 = Button(frame, text="Start Plugin", command=o17).pack()
else:
    pass

if error18 == 0:
    l18 = Label(frame, text=name18, bg="black", fg="white").pack()
    b18 = Label(frame, text=opisanie18, bg="black", fg="white").pack()
    bb18 = Button(frame, text="Start Plugin", command=o18).pack()
else:
    pass

if error19 == 0:
    l19 = Label(frame, text=name19, bg="black", fg="white").pack()
    b19 = Label(frame, text=opisanie19, bg="black", fg="white").pack()
    bb19 = Button(frame, text="Start Plugin", command=o19).pack()
else:
    pass

if error20 == 0:
    l20 = Label(frame, text=name20, bg="black", fg="white").pack()
    b20 = Label(frame, text=opisanie20, bg="black", fg="white").pack()
    bb20 = Button(frame, text="Start Plugin", command=o20).pack()
else:
    pass

if error21 == 0:
    l21 = Label(frame, text=name21, bg="black", fg="white").pack()
    b21 = Label(frame, text=opisanie21, bg="black", fg="white").pack()
    bb21 = Button(frame, text="Start Plugin", command=o21).pack()
else:
    pass

if error22 == 0:
    l22 = Label(frame, text=name22, bg="black", fg="white").pack()
    b22 = Label(frame, text=opisanie22, bg="black", fg="white").pack()
    bb22 = Button(frame, text="Start Plugin", command=o22).pack()
else:
    pass

if error23 == 0:
    l23 = Label(frame, text=name23, bg="black", fg="white").pack()
    b23 = Label(frame, text=opisanie23, bg="black", fg="white").pack()
    bb23 = Button(frame, text="Start Plugin", command=o23).pack()
else:
    pass

if error24 == 0:
    l24 = Label(frame, text=name24, bg="black", fg="white").pack()
    b24 = Label(frame, text=opisanie24, bg="black", fg="white").pack()
    bb24 = Button(frame, text="Start Plugin", command=o24).pack()
else:
    pass

if error25 == 0:
    l5 = Label(frame, text=name25, bg="black", fg="white").pack()
    b5 = Label(frame, text=opisanie25, bg="black", fg="white").pack()
    bb25 = Button(frame, text="Start Plugin", command=o25).pack()
else:
    pass

if error26 == 0:
    l26 = Label(frame, text=name26, bg="black", fg="white").pack()
    b26 = Label(frame, text=opisanie26, bg="black", fg="white").pack()
    bb26 = Button(frame, text="Start Plugin", command=o26).pack()
else:
    pass

if error27 == 0:
    l27 = Label(frame, text=name27, bg="black", fg="white").pack()
    b27 = Label(frame, text=opisanie27, bg="black", fg="white").pack()
    bb27 = Button(frame, text="Start Plugin", command=o27).pack()
else:
    pass

if error28 == 0:
    l28 = Label(frame, text=name28, bg="black", fg="white").pack()
    b28 = Label(frame, text=opisanie28, bg="black", fg="white").pack()
    bb28 = Button(frame, text="Start Plugin", command=o28).pack()
else:
    pass

if error29 == 0:
    l29 = Label(frame, text=name29, bg="black", fg="white").pack()
    b29 = Label(frame, text=opisanie29, bg="black", fg="white").pack()
    bb29 = Button(frame, text="Start Plugin", command=o29).pack()
else:
    pass

if error30 == 0:
    l30 = Label(frame, text=name30, bg="black", fg="white").pack()
    b30 = Label(frame, text=opisanie30, bg="black", fg="white").pack()
    bb30 = Button(frame, text="Start Plugin", command=o30).pack()
else:
    pass

if error31 == 0:
    l31 = Label(frame, text=name31, bg="black", fg="white").pack()
    b31 = Label(frame, text=opisanie31, bg="black", fg="white").pack()
    bb31 = Button(frame, text="Start Plugin", command=o31).pack()
else:
    pass

if error32 == 0:
    l32 = Label(frame, text=name32, bg="black", fg="white").pack()
    b32 = Label(frame, text=opisanie32, bg="black", fg="white").pack()
    bb32 = Button(frame, text="Start Plugin", command=o32).pack()
else:
    pass

def save_file():
    dr = "output photo/"
    nameafile = f"{dr}image_{randint(0, 100000)}.png"
    image1.save(nameafile)
    ms.showinfo("Save", "Saved in output photo")

def close_file():
    r = ms.askyesno("Exit", "Do you want to exit?")
    if r:
        sys.exit()


file_menu = Menu(mmenu, tearoff=0)
file_menu.add_command(label="Plugin Manager", command=vvim)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_file)
mmenu.add_cascade(label="File", menu=file_menu)
win.config(menu=mmenu)

def drawcan(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_line(x1, y1, x2, y2, fill="black", width=5)
    draw.line((x1, y1, x2, y2), fill="black", width=5)

def drawcanfr(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_line(x1, y1, x2, y2, fill="white", width=5)
    draw.line((x1, y1, x2, y2), fill="white", width=5)

with io.open("sourse/selectedfile.txt", "r", encoding="UTF-8") as file:
    filename = file.read()
    image1 = Image.open(filename)
    draw = ImageDraw.Draw(image1)
    photo = ImageTk.PhotoImage(image1)
    draw = ImageDraw.Draw(image1)
    cv = Canvas(win, width=800, height=700, bg="white")
    canvas_width = win.winfo_width()
    canvas_height = win.winfo_height()
    cv.create_image(canvas_width//2, canvas_height//2, image=photo, anchor=CENTER)
    win.photo = photo

cv.bind("<B1-Motion>", drawcan)
cv.bind("<B2-Motion>", drawcanfr)
cv.pack(fill=BOTH, expand=True)

btn = Button(win, text="Save", fg="White", bg="Black")
btn.pack()

win.mainloop()