from pdf2image import convert_from_path
import re
import os
import cv2
import pytesseract

#print(arr)
# Store Pdf with convert_from_path function
"""for filename  in arr:
    images = convert_from_path('cia_pdf/'+filename)
    for img in images:
        img.save(filename.replace('.pdf',''), 'JPEG')
"""
def remove_noise(image):
    return cv2.medianBlur(image,5)

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    img=cv2.imread(filename)
    img=remove_noise(img)
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
try:
    from PIL import Image
except ImportError:
    import Image

arr = os.listdir('cia_png')
print(arr)

for filename  in arr:
    text = ocr_core('cia_png/'+filename)
    f = open('cia_texts/'+filename+".txt", "x")
    f.write(text)
