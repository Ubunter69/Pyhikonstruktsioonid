from tkinter import *
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import ssl
import imghdr
import threading
import time

file = None
dark_mode = False

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    l_lisatud.configure(text=file if file else "Pilt pole valitud")
    return file

def saada_kiri():
    def send():
        btn_saada.config(state=DISABLED)
        laadimine.config(text="Saatmine...")
        kellele = email_sis.get()
        teema = teema_sis.get()
        kiri = kiri_sis.get("1.0", "end").strip()
        allkiri = allkiri_sis.get()
        kiri += f"\n\n{allkiri}" if allkiri else ""

        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "mareklukk8@gmail.com"
        password = "zvnf bbvs fzkd qgfz"

        context = ssl.create_default_context()
        msg = EmailMessage()
        msg.set_content(kiri)
        msg['Subject'] = teema
        msg['From'] = sender_email
        msg['To'] = kellele

        if file:
            try:
                with open(file, 'rb') as fpilt:
                    pilt = fpilt.read()
                    msg.add_attachment(
                        pilt,
                        maintype='image',
                        subtype=imghdr.what(None, pilt)
                    )
            except Exception as e:
                messagebox.showwarning("Hoiatus", f"Pildi lisamine ebaõnnestus: {e}")

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
            messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
        except Exception as e:
            messagebox.showerror("Tekkis viga!", e)
        finally:
            server.quit()
            laadimine.config(text="")
            btn_saada.config(state=NORMAL)

    threading.Thread(target=send).start()

def toggle_teema():
    global dark_mode
    dark_mode = not dark_mode
    bg = "black" if dark_mode else "lightblue"
    fg = "white" if dark_mode else "black"
    aken.config(bg=bg)
    for widget in aken.winfo_children():
        try:
            widget.config(bg=bg, fg=fg)
        except:
            pass
    l_lisatud.config(bg=bg, fg=fg)

def skriimer():
    win = Toplevel()
    win.title("!!!")
    win.geometry("300x300+100+100")
    canvas = Canvas(win, width=300, height=300)
    canvas.pack()
    img = PhotoImage(file="KassScream.png")
    img_id = canvas.create_image(150, 150, image=img)

    def flash():
        for _ in range(6):
            canvas.itemconfigure(img_id, state="hidden")
            time.sleep(0.2)
            canvas.itemconfigure(img_id, state="normal")
            time.sleep(0.2)
        win.destroy()

    threading.Thread(target=flash).start()
    win.mainloop()

# GUI
aken = Tk()
aken.title("E-kirja saatmine")
aken.geometry("500x460")
aken.config(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Untitled.ico")

email = Label(aken, text="EMAIL:", bg="green", width=9, font=("Arial", 16), fg="white")
email_sis = Entry(aken, bg="white", width=21, font=("Arial", 16), fg="black")

teema = Label(aken, text="TEEMA:", bg="green", width=9, font=("Arial", 16), fg="white")
teema_sis = Entry(aken, bg="white", width=21, font=("Arial", 16), fg="black")

lisa = Label(aken, text="LISA:", bg="green", width=9, font=("Arial", 16), fg="white")
l_lisatud = Label(aken, text="Pilt pole valitud", bg="lightblue", font=("Arial", 10), fg="black")

kiri = Label(aken, text="KIRI:", bg="green", width=9, font=("Arial", 16), fg="white")
kiri_sis = Text(aken, bg="white", width=21, height=5, font=("Arial", 16), fg="black")

allkiri_lbl = Label(aken, text="ALLKIRI:", bg="green", width=9, font=("Arial", 16), fg="white")
allkiri_sis = Entry(aken, bg="white", width=21, font=("Arial", 12), fg="black")

btn_vali = Button(aken, text="LISA PILT", command=vali_pilt, bg="green", font=("Arial", 14), fg="white", relief=RAISED)
btn_saada = Button(aken, text="SAADA", command=saada_kiri, bg="green", font=("Arial", 14), fg="white", relief=RAISED)
btn_teema = Button(aken, text="TUME/HELE", command=toggle_teema, bg="gray", font=("Arial", 12), fg="white")
btn_scream = Button(aken, text="SKRIMER", command=skriimer, bg="red", font=("Arial", 12), fg="white")

laadimine = Label(aken, text="", bg="lightblue", font=("Arial", 12), fg="black")

# Paigutus
email.grid(row=1, column=1, pady=5)
email_sis.grid(row=1, column=2)

teema.grid(row=2, column=1, pady=5)
teema_sis.grid(row=2, column=2)

lisa.grid(row=3, column=1, pady=5)
l_lisatud.grid(row=3, column=2)

kiri.grid(row=4, column=1, pady=5, sticky=N)
kiri_sis.grid(row=4, column=2)

allkiri_lbl.grid(row=5, column=1)
allkiri_sis.grid(row=5, column=2)

btn_vali.place(x=120, y=330)
btn_saada.place(x=250, y=330)

btn_teema.place(x=370, y=10)
btn_scream.place(x=370, y=50)
laadimine.place(x=250, y=370)

aken.mainloop()
