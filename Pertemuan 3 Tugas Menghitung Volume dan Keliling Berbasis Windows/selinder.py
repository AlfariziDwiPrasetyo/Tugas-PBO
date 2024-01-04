from tkinter import *
import tkinter as tk
from math import pi

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Alas Bangun Selinder")


def hitung():
    output_hasil_luas_selimut.delete(0, END)
    output_hasil_volume.delete(0, END)
    output_hasil_luas_permukaan.delete(0, END)

    radius = float(entry_radius.get())
    tinggi = float(entry_tinggi.get())

    luas_selimut = 2 * pi * radius * tinggi
    luas_permukaan = 2 * pi * radius * tinggi + 2 * pi * radius ** 2
    volume = pi * radius**2 * tinggi

    output_hasil_luas_selimut.insert(0, round(luas_selimut, 2))
    output_hasil_volume.insert(0, round(volume, 2))
    output_hasil_luas_permukaan.insert(0, round(luas_permukaan, 2))


# Label Nama
label_nama = tk.Label(
    app, text="Al Farizi Dwi Prasetyo (220511019)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Radius
label_radius = tk.Label(app, text="Radius : ")
label_radius.grid(row=1, column=0, padx=5, pady=5)
entry_radius = tk.Entry(app)
entry_radius.grid(row=1, column=2, padx=5, pady=5)

# Tinggi
label_tinggi = tk.Label(app, text="Tinggi : ")
label_tinggi.grid(row=2, column=0, padx=5, pady=5)
entry_tinggi = tk.Entry(app)
entry_tinggi.grid(row=2, column=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung = tk.Button(
    app, text="Hitung", command=hitung, pady=3, padx=3)
hitung.grid(row=4, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas_selimut = tk.Label(app, text="Luas Selimut ", height=2)
label_hasil_luas_selimut.grid(row=6, column=0, padx=5, pady=5)
output_hasil_luas_selimut = tk.Entry(app)
output_hasil_luas_selimut.grid(row=6, column=2, padx=5, pady=5)

label_hasil_luas_permukaan = tk.Label(app, text="Luas Permukaan ", height=2)
label_hasil_luas_permukaan.grid(row=7, column=0, padx=5, pady=5)
output_hasil_luas_permukaan = tk.Entry(app)
output_hasil_luas_permukaan.grid(row=7, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
label_hasil_volume.grid(row=8, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=8, column=2, padx=5, pady=5)


app.mainloop()
