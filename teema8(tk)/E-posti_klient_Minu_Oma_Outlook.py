from tkinter import *
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import ssl
import imghdr

file = None  # et vältida NameError

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    l_lisatud.configure(text=file if file else "Pilt pole valitud")
    return file

def saada_kiri():
    kellele = email_sis.get()
    teema = teema_sis.get()
    kiri = kiri_sis.get("1.0", "end")

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "mareklukk8@gmail.com"
    password = "zvnf bbvs fzkd qgfz"  # Gmail rakenduse parool!

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

# --- GUI ---
aken = Tk()
aken.title("E-kirja saatmine")
aken.geometry("500x420")
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

lisa_pilt = Button(aken, text="LISA PILT", command=vali_pilt, bg="green", font=("Arial", 14), fg="white", relief=RAISED)
saada_e = Button(aken, text="SAADA", command=saada_kiri, bg="green", font=("Arial", 14), fg="white", relief=RAISED)

# Paigutus
email.grid(row=1, column=1, pady=5)
email_sis.grid(row=1, column=2)

teema.grid(row=2, column=1, pady=5)
teema_sis.grid(row=2, column=2)

lisa.grid(row=3, column=1, pady=5)
l_lisatud.grid(row=3, column=2)

kiri.grid(row=4, column=1, pady=5, sticky=N)
kiri_sis.grid(row=4, column=2)

lisa_pilt.place(x=120, y=260)
saada_e.place(x=250, y=260)

aken.mainloop()
