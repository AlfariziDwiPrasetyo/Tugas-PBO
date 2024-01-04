import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        return Image.open(file_path)
    return None


def image_to_text():
    img = open_image()
    if img:
        text = pytesseract.image_to_string(img)
        text_output.delete('1.0', tk.END)  # Clear previous text
        text_output.insert(tk.END, text)
        img.thumbnail((300, 300))  # Resizing image for display
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img


root = tk.Tk()
root.title("Image to Text Converter")

img_label = tk.Label(root)
img_label.pack()

convert_button = tk.Button(root, text="Convert to Text", command=image_to_text)
convert_button.pack(padx=10, pady=5)

text_output = tk.Text(root, height=10, width=50)
text_output.pack(padx=10, pady=5)

root.mainloop()
