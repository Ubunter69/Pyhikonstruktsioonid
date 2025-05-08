from tkinter import *
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import ssl
import imghdr

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    l_lisatud.configure(text=file)
    return file

def saada_kiri():
    kellele = email_sis.get()
    teema = teema_sis.get()
    kiri = kiri_sis.get("1.0", "end")

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

    try:
        with open(file, 'rb') as fpilt:
            pilt = fpilt.read()
            msg.add_attachment(
                pilt,
                maintype='image',
                subtype=imghdr.what(None, pilt)
            )
    except:
        messagebox.showwarning("Hoiatus", "Pilt pole valitud või faili ei saa avada!")

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

# GUI
aken = Tk()
aken.title("E-kirja saatmine")
aken.geometry("450x400")
aken.config(bg="lightblue")
aken.resizable(width=False, height=False)
aken.iconbitmap("Untitled.ico")

# Valikud
email = Label(aken, text="EMAIL:", bg="green", width=9, font=("Arial", 16), fg="white")
email_sis = Entry(aken, bg="white", width=25, font=("Arial", 16), fg="black")

teema = Label(aken, text="TEEMA:", bg="green", width=9, font=("Arial", 16), fg="white")
teema_sis = Entry(aken, bg="white", width=25, font=("Arial", 16), fg="black")

lisa = Label(aken, text="LISA:", bg="green", width=9, font=("Arial", 16), fg="white")
l_lisatud = Label(aken, text="Pilt pole valitud", bg="lightblue", font=("Arial", 12), fg="black")

kiri = Label(aken, text="KIRI:", bg="green", width=9, font=("Arial", 16), fg="white")
kiri_sis = Text(aken, bg="white", width=25, height=6, font=("Arial", 14), fg="black")


btn_vali = Button(aken, text="Vali pilt", command=vali_pilt, font=("Arial", 14), bg="green", fg="white")
btn_saada = Button(aken, text="Saada kiri", command=saada_kiri, font=("Arial", 14), bg="green", fg="white")


email.grid(row=0, column=0, padx=10, pady=10, sticky=E)
email_sis.grid(row=0, column=1, padx=10)

teema.grid(row=1, column=0, padx=10, pady=10, sticky=E)
teema_sis.grid(row=1, column=1, padx=10)

lisa.grid(row=2, column=0, padx=10, pady=10, sticky=E)
l_lisatud.grid(row=2, column=1, padx=10)

kiri.grid(row=3, column=0, padx=10, pady=10, sticky=NE)
kiri_sis.grid(row=3, column=1, padx=10)

btn_vali.grid(row=4, column=1,)
btn_saada.grid(row=5, column=1,)

aken.mainloop()
