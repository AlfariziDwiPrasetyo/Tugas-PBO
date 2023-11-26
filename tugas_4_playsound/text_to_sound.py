import tkinter as tk
from gtts import gTTS
import pygame


def text_to_sound():

    def convert_text_to_sound():

        # Mendapatkan teks dari input pengguna
        mytext = entry.get()

        # Memastikan teks tidak kosong sebelum melanjutkan
        if not mytext:
            mytext = "tidak ada perintah"
            return mytext

        language = 'id'
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Save the sound file
        myobj.save("media/Sounds.mp3")

        # Play the sound using pygame
        pygame.mixer.init()
        pygame.mixer.music.load("media/Sounds.mp3")
        pygame.mixer.music.play()

    # Membuat jendela Tkinter
    root = tk.Tk()
    root.title("Text to Sound")

    # Membuat label dan input untuk memasukkan teks
    label = tk.Label(root, text="Masukkan teks:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    # Membuat tombol untuk mengonversi teks ke suara
    button = tk.Button(root, text="Konversi ke Suara",
                       command=convert_text_to_sound)
    button.pack(pady=10)

    # Menjalankan loop utama Tkinter
    root.mainloop()
