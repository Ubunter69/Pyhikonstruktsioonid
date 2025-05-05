from tkinter import *
k=0
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!")
    nupp.config(text="Vajuta veel kord!", bg="orange",
    fg="blue")
def vajutatudPK(event):
    global k 
    k-=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!")
    nupp.config(text="Vajuta veel kord!", bg="orange", fg="orange")


def tuhista(event):
    sisestus.delete(0, END)
    #sisestus.unbind("<FocusIn>")
    #sisestus.bind("<FocusOut>", tagasi)



aken=Tk()
aken.title("Teema8")
aken.geometry("400x400")
aken.config(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Untitled.ico")
pealkiri=Label(aken, text="Tere tulemast!",bg="blue", font=("Arial", 16),fg="green")
#fg - цвет текста
nupp=Button(aken, text="Vajuta mind!", bg="red", font=("Arial", 12), fg="white", relief=RAISED, command=vajutatud)#SUNKEN, RASED, GROOVE, and RIDGE
nupp.bind("<Button-3>", vajutatudPK)
sisestus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
sisestus.insert(0, "Sisesta midagi siia") #END можно добавить вместо нуля
sisestus.bind("<FocusIn>", tuhista)






pealkiri.pack(pady=20)
sisestus.pack(pady=20)
nupp.pack(pady=20)








aken.mainloop()




