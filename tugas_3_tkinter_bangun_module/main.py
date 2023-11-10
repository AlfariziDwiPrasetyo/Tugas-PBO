import tkinter as tk
from app import *


def on_option_selected(event):
    selected_option = option_var.get()

    if selected_option == "Balok":
        balok()
    elif selected_option == "Bola":
        bola()
    elif selected_option == "Kerucut":
        kerucut()
    elif selected_option == "Kubus":
        kubus()
    elif selected_option == "Limas Segiempat":
        limas_segiempat()
    elif selected_option == "Limas Segitiga":
        limas_segitiga()
    elif selected_option == "Prisma Segitiga":
        prisma_segitiga()
    elif selected_option == "Selinder":
        selinder()


# Membuat jendela tkinter
app = tk.Tk()
app.title("Pilih Bentuk Bangun")
app.minsize(width=500, height=100)

# Label untuk keterangan
label = tk.Label(app, text="Pilih bentuk bangun:")
label.grid(column=1, row=3)

# Daftar opsi bentuk bangun
options = ["Balok", "Bola", "Kerucut", "Kubus",
           "Limas Segiempat", "Limas Segitiga", "Prisma Segitiga", "Selinder"]

# Variable tkinter untuk menyimpan opsi yang dipilih
option_var = tk.StringVar(app)
option_var.set(options[0])

# Membuat OptionMenu dan mengaitkannya dengan option_var
option_menu = tk.OptionMenu(app, option_var, *options)
option_menu.grid(column=2, row=3)

# Tombol untuk menampilkan jendela yang sesuai
show_option_button = tk.Button(
    app, text="Tampilkan", command=lambda event=None: on_option_selected(event))
show_option_button.grid(column=3, row=3)

app.mainloop()
