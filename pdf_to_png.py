from pdf2image import convert_from_path
import re
import os
import cv2
import pytesseract
arr = os.listdir('cia_png')
#print(arr)
# Store Pdf with convert_from_path function
for filename  in arr:
    images = convert_from_path('cia_pdf/'+filename)
    for img in images:
        img.save(filename.replace('.pdf',''), 'JPEG')
