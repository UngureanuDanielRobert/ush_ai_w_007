import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def ocr_extractor(image_path, language='ron'):
    # Open image
    image = Image.open(image_path)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(image, lang=language)
    
    return text

def select_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path:
        # Get selected language
        lang = simpledialog.askstring("Language", "Introduceti limba textului din imagine (pentru limba Romana scrieti 'ron'):")
        if lang:
            text = ocr_extractor(file_path, lang)
        else:
            text = ocr_extractor(file_path)
        print(text)
    else:
        print("Error: No file selected.")

select_image()