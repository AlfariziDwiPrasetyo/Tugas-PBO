import tkinter as tk
from image_to_text import image_to_text
from mp3_app import mp3_app
from mp4_app import mp4_app
from text_to_sound import text_to_sound


def on_option_selected(event):
    selected_option = option_var.get()

    if selected_option == "gambar ke teks":
        image_to_text()
    elif selected_option == "Play king gnu - specialz":
        mp3_app()
    elif selected_option == "Kimi No Nawa - Trailer":
        mp4_app()
    elif selected_option == "text ke suara":
        text_to_sound()
    else:
        print("Maaf Fitur belum tersedia")


# Membuat jendela tkinter
app = tk.Tk()
app.title("App Untuk Tugas 4")
app.minsize(width=500, height=100)

# Label untuk keterangan
label = tk.Label(app, text="Pilih mau melakukan aktivitas apa :")
label.grid(column=1, row=3)

# Daftar opsi bentuk bangun
options = ["gambar ke teks", "Play king gnu - specialz",
           "Kimi No Nawa - Trailer", "text ke suara",]

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
