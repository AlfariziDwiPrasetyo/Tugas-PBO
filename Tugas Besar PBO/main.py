import tkinter as tk
from tkinter import messagebox
import mysql.connector as mc
from db import DBConnection


# untuk membuat tabel pada mysql jik belum ada tabel 'menabung_uang'
DBConnection()


class MyTabungan:
    def __init__(self, root):
        self._nama = None
        self.root = root
        self.root.title("MyTabungan")
        self.root.geometry("400x300")
        self.db = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="mytabungan"
        )

        self.login_frame = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root)

        self.create_login_widgets()
        self.create_main_widgets()

        self.show_login_page()

    def create_login_widgets(self):

        # User interface untuk halaman login
        label_nama = tk.Label(self.login_frame, text="Username : ")
        label_nama.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nama = tk.Entry(self.login_frame)
        self.entry_nama.grid(row=1, column=0, padx=10, pady=10)

        login_button = tk.Button(
            self.login_frame, text="Login", command=self.register_or_login)
        login_button.grid(row=3, column=0, padx=10, pady=10)

    def create_main_widgets(self):

        # User interface untuk halaman utama
        self.label_nama = tk.Label(self.main_frame, font=("arial", 16))
        self.label_nama.pack(anchor="center", padx=10, pady=10)

        self.label_saldo = tk.Label(self.main_frame, font=("arial", 16))
        self.label_saldo.pack(anchor="center", padx=10, pady=10)

        self.entry_uang = tk.Entry(self.main_frame)
        self.entry_uang.pack(anchor="center", padx=10, pady=10)

        self.button_tambah = tk.Button(
            self.main_frame, text="Tabung Uang", command=self.tambah_uang)
        self.button_tambah.pack(anchor="center", padx=10, pady=10)

        self.button_ambil = tk.Button(
            self.main_frame, text="Ambil Uang", command=self.ambil_uang)
        self.button_ambil.pack(anchor="center", padx=10, pady=10)

    def show_login_page(self):
        self.main_frame.pack_forget()
        self.login_frame.pack()

    def show_main_page(self):
        self.login_frame.pack_forget()
        self.main_frame.pack()

    def register_or_login(self):
        nama = self.entry_nama.get()
        cursor = self.db.cursor()

        if nama == '':
            messagebox.showwarning("Peringatan", "Harap isi field nama.")
            return
        else:

            cursor.execute(
                f"SELECT * FROM menabung_uang WHERE nama = '{nama}'")
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showinfo(
                    "Login Berhasil", f"Selamat datang, {nama}!")
                self.show_main_page()
                self.display_main(nama)
                self.display_nama(nama)
                self._nama = nama
            else:
                cursor.execute(
                    f"INSERT INTO menabung_uang (nama, saldo) VALUES ('{nama}', 0)")
                self.db.commit()
                messagebox.showinfo(
                    "Registrasi Berhasil", f"Registrasi berhasil untuk {nama}, saldo awal anda adalah 0")
                self.show_main_page()
                self.display_main(nama)
                self.display_nama(nama)
                self._nama = nama

    def display_main(self, nama):
        try:
            cursor = self.db.cursor()
            cursor.execute(
                f"SELECT saldo FROM menabung_uang WHERE nama = '{nama}'")
            result = cursor.fetchone()
            if result:
                saldo = result[0]
                self.label_saldo.config(text=f"Rp. {saldo}")
            else:
                self.label_saldo.config(text="No data found")
        except Exception as e:
            print(f"Error occurred: {e}")

    def display_nama(self, nama):
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT nama FROM menabung_uang WHERE nama = '{nama}'")
        nama = cursor.fetchone()[0]
        self.label_nama.config(text=f"Selamat Datang, {nama}")

    def tambah_uang(self):
        nama = self._nama
        uang = self.entry_uang.get()
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT saldo FROM menabung_uang WHERE nama = '{nama}'")
        saldo = cursor.fetchone()[0]
        tabung_uang = int(saldo) + int(uang)
        cursor.execute(
            f"UPDATE menabung_uang SET saldo = '{tabung_uang}' WHERE nama = '{nama}'")
        self.db.commit()
        messagebox.showinfo(
            "Uang Berhasil Di Tabung", f"Berhasil menabung {uang}")
        self.display_main(nama)

    def ambil_uang(self):
        nama = self._nama
        uang = self.entry_uang.get()
        cursor = self.db.cursor()
        cursor.execute(
            f"SELECT saldo FROM menabung_uang WHERE nama = '{nama}'")
        saldo = cursor.fetchone()[0]
        ambil_uang = int(saldo) - int(uang)
        if ambil_uang < 0:
            messagebox.showwarning("Peringatan", "Saldo Anda Kurang")
        else:
            cursor.execute(
                f"UPDATE menabung_uang SET saldo = '{ambil_uang}' WHERE nama = '{nama}'")
            self.db.commit()
            messagebox.showinfo(
                "Uang Berhasil Di Ambil", f"Berhasil mengambil {uang}")
            self.display_main(nama)


root = tk.Tk()
app = MyTabungan(root)
root.mainloop()
