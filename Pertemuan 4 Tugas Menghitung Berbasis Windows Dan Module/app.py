from tkinter import *
import tkinter as tk
from rumus import *


def balok():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Balok")

    def hitung():
        output_hasil_luas.delete(0, END)
        output_hasil_volume.delete(0, END)

        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        luas = luas_balok(panjang, lebar, tinggi)
        volume = volume_balok(panjang, lebar, tinggi)
        output_hasil_luas.insert(0, round(luas, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Panjang
    label_panjang = tk.Label(app, text="Panjang Balok : ")
    label_panjang.grid(row=1, column=0, padx=5, pady=5)
    entry_panjang = tk.Entry(app)
    entry_panjang.grid(row=1, column=2, padx=5, pady=5)

    # Lebar
    label_lebar = tk.Label(app, text="lebar Balok : ")
    label_lebar.grid(row=2, column=0, padx=5, pady=5)
    entry_lebar = tk.Entry(app)
    entry_lebar.grid(row=2, column=2, padx=5, pady=5)

    # Tinggi
    label_tinggi = tk.Label(app, text="tinggi Balok : ")
    label_tinggi.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_tinggi = tk.Entry(app)
    entry_tinggi.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # button nya
    spacer = tk.Label(app, text="")
    spacer.grid()
    hitung = tk.Button(
        app, text="Hitung", command=hitung, pady=3, padx=3)
    hitung.grid(row=4, column=2, padx=5, pady=5)

    # output hasilnya
    label_hasil_luas = tk.Label(app, text="Luas ", height=2)
    label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas = tk.Entry(app)
    output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def bola():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Bola")

    def hitung():
        output_hasil_luas.delete(0, END)
        output_hasil_volume.delete(0, END)

        radius = float(entry_radius.get())
        luas = luas_bola(radius)
        volume = volume_bola(radius)
        output_hasil_luas.insert(0, round(luas, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Radius
    label_radius = tk.Label(app, text="Radius Bola : ")
    label_radius.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_radius = tk.Entry(app)
    entry_radius.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # button nya
    spacer = tk.Label(app, text="")
    spacer.grid()
    hitung = tk.Button(
        app, text="Hitung", command=hitung, pady=3, padx=3)
    hitung.grid(row=4, column=2, padx=5, pady=5)

    # output hasilnya
    label_hasil_luas = tk.Label(app, text="Luas : ", height=2)
    label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas = tk.Entry(app)
    output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def kerucut():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Kerucut")

    def hitung():
        output_hasil_luas_selimut.delete(0, END)
        output_hasil_volume.delete(0, END)

        jari_jari = float(entry_jari_jari.get())
        sisi = float(entry_sisi.get())
        tinggi = float(entry_tinggi.get())
        luas_selimut = luas_selimut_kerucut(jari_jari, sisi)
        volume = volume_kerucut(jari_jari, sisi)
        output_hasil_luas_selimut.insert(0, round(luas_selimut, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Jari Jari
    label_jari_jari = tk.Label(app, text="Jari Jari Kerucut : ")
    label_jari_jari.grid(row=1, column=0, padx=5, pady=5)
    entry_jari_jari = tk.Entry(app)
    entry_jari_jari.grid(row=1, column=2, padx=5, pady=5)

    # Sisi
    label_sisi = tk.Label(app, text="Sisi Kerucut : ")
    label_sisi.grid(row=2, column=0, padx=5, pady=5)
    entry_sisi = tk.Entry(app)
    entry_sisi.grid(row=2, column=2, padx=5, pady=5)

    # Tinggi
    label_tinggi = tk.Label(app, text="tinggi Kerucut : ")
    label_tinggi.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_tinggi = tk.Entry(app)
    entry_tinggi.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

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

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def kubus():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Kubus")

    def hitung():
        output_hasil_luas.delete(0, END)
        output_hasil_volume.delete(0, END)

        rusuk = float(entry_rusuk.get())
        luas = luas_kubus(rusuk)
        volume = volume_kubus(rusuk)
        output_hasil_luas.insert(0, round(luas, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Rusuk
    label_rusuk = tk.Label(app, text="Rusuk Kubus : ")
    label_rusuk.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_rusuk = tk.Entry(app)
    entry_rusuk.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # button nya
    spacer = tk.Label(app, text="")
    spacer.grid()
    hitung = tk.Button(
        app, text="Hitung", command=hitung, pady=3, padx=3)
    hitung.grid(row=4, column=2, padx=5, pady=5)

    # output hasilnya
    label_hasil_luas = tk.Label(app, text="Luas : ", height=2)
    label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas = tk.Entry(app)
    output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def limas_segiempat():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Limas Segiempat")

    def hitung():
        output_hasil_luas.delete(0, END)
        output_hasil_volume.delete(0, END)

        panjang = float(entry_panjang.get())
        tinggi = float(entry_tinggi.get())
        volume = volume_limas_segiempat(panjang, tinggi)
        luas = luas_limas_segiempat(panjang, tinggi)
        output_hasil_luas.insert(0, round(luas, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Panjang
    label_panjang = tk.Label(app, text="Panjang Limas : ")
    label_panjang.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_panjang = tk.Entry(app)
    entry_panjang.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # Tinggi
    label_tinggi = tk.Label(app, text="Tinggi Limas : ")
    label_tinggi.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    entry_tinggi = tk.Entry(app)
    entry_tinggi.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

    # button nya
    spacer = tk.Label(app, text="")
    spacer.grid()
    hitung = tk.Button(
        app, text="Hitung", command=hitung, pady=3, padx=3)
    hitung.grid(row=5, column=2, padx=5, pady=5)

    # output hasilnya
    label_hasil_luas = tk.Label(app, text="Luas : ", height=2)
    label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas = tk.Entry(app)
    output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def limas_segitiga():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Limas Segitiga")

    def hitung():
        output_hasil_luas.delete(0, END)
        output_hasil_volume.delete(0, END)

        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        ls = 0.5 * alas * tinggi

        luas = luas_limas_segitiga(alas, tinggi)
        volume = volume_limas_segitiga(alas, tinggi)
        output_hasil_luas.insert(0, round(luas, 2))
        output_hasil_volume.insert(0, round(volume, 2))

    # Label Nama
    label_nama = tk.Label(
        app, text="Al Farizi Dwi Prasetyo (220511019)")
    label_nama.grid(row=0, column=2, padx=5, pady=5)

    # Alas Limas
    label_alas = tk.Label(app, text="Alas Limas :")
    label_alas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    entry_alas = tk.Entry(app)
    entry_alas.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # Tinggi Limas
    label_tinggi = tk.Label(app, text="Tinggi Limas :")
    label_tinggi.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    entry_tinggi = tk.Entry(app)
    entry_tinggi.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

    # button nya
    spacer = tk.Label(app, text="")
    spacer.grid()
    hitung = tk.Button(
        app, text="Hitung", command=hitung, pady=3, padx=3)
    hitung.grid(row=5, column=2, padx=5, pady=5)

    # output hasilnya
    label_hasil_luas = tk.Label(app, text="Luas :", height=2)
    label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas = tk.Entry(app)
    output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume :", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def prisma_segitiga():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Prisma Segitiga")

    def hitung():
        output_hasil_luas_permukaan.delete(0, END)
        output_hasil_volume.delete(0, END)

        tinggi_prisma = float(entry_tinggi_prisma.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        alas = float(entry_alas.get())
        luas_permukaan = luas_permukaan_prisma_segitiga(
            alas, tinggi_prisma, tinggi_segitiga)
        volume = volume_prisma_segitiga(alas, tinggi_prisma, tinggi_segitiga)

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
    label_hasil_luas_permukaan = tk.Label(
        app, text="Luas Permukaan ", height=2)
    label_hasil_luas_permukaan.grid(row=6, column=0, padx=5, pady=5)
    output_hasil_luas_permukaan = tk.Entry(app)
    output_hasil_luas_permukaan.grid(row=6, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

    app.mainloop()


def selinder():
    app = tk.Tk()
    app.minsize(width=500, height=400)
    app.title("Luas Dan Alas Bangun Selinder")

    def hitung():
        output_hasil_luas_selimut.delete(0, END)
        output_hasil_volume.delete(0, END)
        output_hasil_luas_permukaan.delete(0, END)

        radius = float(entry_radius.get())
        tinggi = float(entry_tinggi.get())

        luas_selimut = luas_selimut_selinder(radius, tinggi)
        luas_permukaan = luas_permukaan_selinder(radius, tinggi)
        volume = volume_selinder(radius, tinggi)

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

    label_hasil_luas_permukaan = tk.Label(
        app, text="Luas Permukaan ", height=2)
    label_hasil_luas_permukaan.grid(row=7, column=0, padx=5, pady=5)
    output_hasil_luas_permukaan = tk.Entry(app)
    output_hasil_luas_permukaan.grid(row=7, column=2, padx=5, pady=5)

    label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
    label_hasil_volume.grid(row=8, column=0, padx=5, pady=5)
    output_hasil_volume = tk.Entry(app)
    output_hasil_volume.grid(row=8, column=2, padx=5, pady=5)

    app.mainloop()
