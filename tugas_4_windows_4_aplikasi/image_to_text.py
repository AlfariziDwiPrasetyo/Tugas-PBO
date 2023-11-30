from PIL import Image
from pytesseract import pytesseract


def image_to_text():

    # Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Define path to image
    path_to_image = 'media/gambar2.jpg'

    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    # Open image with PIL
    img = Image.open(path_to_image)

    # Extract text from image
    text = pytesseract.image_to_string(img)

    print(text)
