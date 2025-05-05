from tkinter import *
﻿import numpy as np
import matplotlib.pyplot as plt
def lahenda():
    try:
        a = float(sisestus.get())
        b = float(sisestus1.get())
        c = float(sisestus2.get())
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            vastus.config(text=f"Lahendused: \nx1={x1:.2f}\nx2={x2:.2f}\nD={d}")
        elif d == 0:
            x = -b / (2 * a)
            vastus.config(text=f"Üks lahendus: {x:.2f}")
        else:
            vastus.config(text="Lahendusi pole!")
    except ValueError:
        vastus.config(text="Sisesta numbrid õigesti!")




aken=Tk()
aken.title("Квадратные уравнения")
aken.geometry("520x300")
aken.config(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Untitled.ico")
pealkiri=Label(aken, text="Ruutvorrandi lahendus",bg="blue", font=("Arial", 16),fg="green")
#side=LEFT
sisestus=Entry(aken, bg="white",width=4, font=("Arial", 16), fg="black", )
näidis=Label(aken, text="x**2+", bg="lightblue", font=("Arial", 16),fg="green")
sisestus1=Entry(aken, bg="white",width=4, font=("Arial", 16), fg="black", )
näidis1=Label(aken, text="x+", bg="lightblue", font=("Arial", 16),fg="green")
sisestus2=Entry(aken, bg="white",width=4, font=("Arial", 16), fg="black", )
näidis2=Label(aken, text="=0", bg="lightblue", font=("Arial", 16),fg="green")
nupp=Button(aken, text="Otsustama", bg="red", font=("Arial", 12), fg="white", relief=RAISED, command=lahenda)
vastus=Label(aken, text="lahendus", bg="yellow", font=("Arial", 16), fg="black", )





pealkiri.pack(pady=20)
sisestus.pack(pady=20 , side=LEFT)
näidis.pack(pady=20, side=LEFT)
sisestus1.pack(pady=20, side=LEFT)
näidis1.pack(pady=20, side=LEFT)
sisestus2.pack(pady=20, side=LEFT)
näidis2.pack(pady=20, side=LEFT)
nupp.pack(pady=20, side=LEFT)
vastus.place(x=200, y=200)





#высота в строках и ширина в символах
aken.mainloop()