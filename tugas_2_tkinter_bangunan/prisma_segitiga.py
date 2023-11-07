from tkinter import *
import tkinter as tk
from math import pi

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Alas Bangun Prisma Segitiga")


def hitung():
    output_hasil_luas_permukaan.delete(0, END)
    output_hasil_volume.delete(0, END)

    tinggi_prisma = float(entry_tinggi_prisma.get())
    tinggi_segitiga = float(entry_tinggi_segitiga.get())
    alas = float(entry_alas.get())

    keliling_segitiga = alas**3
    luas_alas = keliling_segitiga * tinggi_prisma
    luas_permukaan = luas_alas + alas * tinggi_segitiga
    volume = (1/2) * alas * tinggi_segitiga * tinggi_prisma

    output_hasil_luas_permukaan.insert(0, round(luas_permukaan, 2))
    output_hasil_volume.insert(0, round(volume, 2))


# Label Nama
label_nama = tk.Label(
    app, text="Al Farizi Dwi Prasetyo (220511019)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Jari Jari
label_tinggi_segitiga = tk.Label(app, text="Tinggi Segitiga : ")
label_tinggi_segitiga.grid(row=1, column=0, padx=5, pady=5)
entry_tinggi_segitiga = tk.Entry(app)
entry_tinggi_segitiga.grid(row=1, column=2, padx=5, pady=5)

# Tinggi Prisma
label_tinggi_prisma = tk.Label(app, text="Tinggi Prisma : ")
label_tinggi_prisma.grid(row=2, column=0, padx=5, pady=5)
entry_tinggi_prisma = tk.Entry(app)
entry_tinggi_prisma.grid(row=2, column=2, padx=5, pady=5)

# Alas
label_alas = tk.Label(app, text="Alas : ")
label_alas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_alas = tk.Entry(app)
entry_alas.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung = tk.Button(
    app, text="Hitung", command=hitung, pady=3, padx=3)
hitung.grid(row=4, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas_permukaan = tk.Label(app, text="Luas Permukaan ", height=2)
label_hasil_luas_permukaan.grid(row=6, column=0, padx=5, pady=5)
output_hasil_luas_permukaan = tk.Entry(app)
output_hasil_luas_permukaan.grid(row=6, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)


app.mainloop()
