import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from Perawat import Perawat


class FormPerawat:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = False
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='NIP:').grid(
            row=0, column=0, sticky=W, padx=5, pady=5)
        self.textNIP = Entry(mainFrame)
        self.textNIP.grid(row=0, column=1, padx=5, pady=5)
        # menambahkan event Enter key
        self.textNIP.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama:').grid(
            row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Jenis Kelamin:').grid(
            row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki',
                             value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select()  # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan',
                             value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan',
                                command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear',
                               command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus',
                               command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idprwt', 'nip', 'nama', 'jk')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idprwt', text='ID')
        self.tree.column('idprwt', width="30")
        self.tree.heading('nip', text='NIP')
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.textNIP.delete(0, END)
        self.textNIP.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data mahasiswa
        prwt = Perawat()
        result = prwt.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        perawat = []
        for row_data in result:
            perawat.append(row_data)

        for student in perawat:
            self.tree.insert('', END, values=student)

    def onCari(self, event=None):
        nip = self.textNIP.get()
        prwt = Perawat()
        res = prwt.getByNIP(nip)
        rec = prwt.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            self.txtNama.focus()
        return res

    def TampilkanData(self, event=None):
        nip = self.textNIP.get()
        prwt = Perawat()
        res = prwt.getByNIP(nip)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, prwt.nama)
        jk = prwt.jk
        if (jk == "P"):
            self.P.select()
        else:
            self.L.select()

        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        nip = self.textNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()

        self.onCari()
        prwt = Perawat()
        prwt.nip = nip
        prwt.nama = nama
        prwt.jk = jk
        if (self.ditemukan == True):
            res = prwt.updateByNIP(nip)
            ket = 'Diperbarui'
        else:
            res = prwt.simpan()
            ket = 'Disimpan'

        rec = prwt.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip = self.textNIP.get()
        self.onCari()
        prwt = Perawat()
        prwt.nip = nip
        if (self.ditemukan == True):
            res = prwt.deleteByNIP(nip)
            rec = prwt.affected
        else:
            messagebox.showinfo(
                "showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0

        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPerawat(root, "Aplikasi Data Perawat")
    root.mainloop()
