import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from MataKuliah import MataKuliah


class FormMatkul:

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

        # KODE MK
        Label(mainFrame, text='Kode Mk:').grid(
            row=0, column=0, sticky=W, padx=5, pady=5)
        self.textKodeMK = Entry(mainFrame)
        self.textKodeMK.grid(row=0, column=1, padx=5, pady=5)

        # NAMA MK
        Label(mainFrame, text='Nama MK:').grid(
            row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        # SKS MK
        Label(mainFrame, text='SKS:').grid(
            row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtSks = StringVar()
        self.sks2 = Radiobutton(mainFrame, text='2 SKS',
                                value=2, variable=self.txtSks)
        self.sks2.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.sks2.select()
        self.sks3 = Radiobutton(mainFrame, text='3 SKS',
                                value=3, variable=self.txtSks)
        self.sks3.grid(row=2, column=2, padx=5, pady=5, sticky=W)

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
        columns = ('idmatkul', 'Kode MK', 'nama', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmatkul', text='ID')
        self.tree.column('idmatkul', width="30")
        self.tree.heading('Kode MK', text='Kode MK')
        self.tree.column('Kode MK', width="60")
        self.tree.heading('nama', text='Nama MK')
        self.tree.column('nama', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.textKodeMK.delete(0, END)
        self.textKodeMK.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")
        self.sks2.select()
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data matkul
        matkul = MataKuliah()
        result = matkul.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        matkul = []
        for row_data in result:
            matkul.append(row_data)

        for pwt in matkul:
            self.tree.insert('', END, values=pwt)

    def onCari(self, event=None):
        kodeMk = self.textKodeMK.get()
        matkul = MataKuliah()
        res = matkul.getByKodeMk(kodeMk)
        rec = matkul.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            # self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            self.txtNama.focus()
        return res

    def TampilkanData(self, event=None):
        kodeMk = self.textKodeMK.get()
        matkul = MataKuliah()
        res = matkul.getByKodeMk(kodeMk)
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, matkul.mk)
        sks = matkul.sks
        if (sks == 2):
            self.sks2.select()
        else:
            self.sks3.select()

        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kodeMk = self.textKodeMK.get()
        nama = self.txtNama.get()
        sks = self.txtSks.get()
        self.onCari()
        matkul = MataKuliah()
        matkul.kodemk = kodeMk
        matkul.mk = nama
        matkul.sks = sks

        if (self.ditemukan == True):
            res = matkul.updateByKodeMk(kodeMk)
            ket = 'Diperbarui'
        else:
            print("Halo")
            res = matkul.simpan()
            ket = 'Disimpan'

        rec = matkul.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodeMk = self.textKodeMK.get()
        self.onCari()
        matkul = MataKuliah()
        matkul.kodemk = kodeMk
        if (self.ditemukan == True):
            res = matkul.deleteByKodeMk(kodeMk)
            rec = matkul.affected
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
    aplikasi = FormMatkul(root, "Aplikasi Manajemen Mata Kuliah")
    root.mainloop()
