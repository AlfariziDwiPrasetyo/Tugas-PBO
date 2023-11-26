import tkinter as tk

def convert_temperature():
    try:
        # Mengambil input pengguna
        input_suhu = float(entry_suhu.get())

        if selected_unit.get() == "Celsius":
            # Konversi ke Fahrenheit dan Kelvin dari Celsius
            fahrenheit = (input_suhu * 9/5) + 32
            kelvin = input_suhu + 273.15

            # Menampilkan hasil konversi
            label_fahrenheit.config(text=f"{fahrenheit:.2f} °F")
            label_kelvin.config(text=f"{kelvin:.2f} K")
        elif selected_unit.get() == "Fahrenheit":
            # Konversi ke Celsius dan Kelvin dari Fahrenheit
            celsius = (input_suhu - 32) * 5/9
            kelvin = (input_suhu + 459.67) * 5/9

            # Menampilkan hasil konversi
            label_fahrenheit.config(text=f"{celsius:.2f} °C")
            label_kelvin.config(text=f"{kelvin:.2f} K")
        elif selected_unit.get() == "Kelvin":
            # Konversi ke Celsius dan Fahrenheit dari Kelvin
            celsius = input_suhu - 273.15
            fahrenheit = (input_suhu * 9/5) - 459.67

            # Menampilkan hasil konversi
            label_fahrenheit.config(text=f"{celsius:.2f} °C")
            label_kelvin.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        # Menampilkan pesan kesalahan jika input tidak valid
        label_fahrenheit.config(text="Masukkan angka yang valid")
        label_kelvin.config(text="Masukkan angka yang valid")

# Membuat instance Tkinter
root = tk.Tk()
root.title("Konversi Suhu")

# Pilihan unit suhu
units = ["Celsius", "Fahrenheit", "Kelvin"]
selected_unit = tk.StringVar()
selected_unit.set(units[0])  # Mengatur nilai awal pilihan

# Membuat label dan menu dropdown untuk pilihan unit suhu
label_unit = tk.Label(root, text="Pilih Satuan Suhu:")
label_unit.pack()

unit_menu = tk.OptionMenu(root, selected_unit, *units)
unit_menu.pack()

# Membuat label dan entry untuk input suhu
label_input = tk.Label(root, text="Masukkan Suhu:")
label_input.pack()

entry_suhu = tk.Entry(root)
entry_suhu.pack()

# Membuat tombol konversi
button_convert = tk.Button(root, text="Konversi", command=convert_temperature)
button_convert.pack()

# Membuat label untuk menampilkan hasil konversi
label_fahrenheit = tk.Label(root, text="")
label_fahrenheit.pack()

label_kelvin = tk.Label(root, text="")
label_kelvin.pack()

# Menjalankan aplikasi
root.mainloop()
