from PIL import Image
from pytesseract import pytesseract
import cv2
from pytesseract import pytesseract

image = Image.open('e3.png')
image = image.resize((400,200))
image.save('sample.png')

path_to_tesseract = r'C:\Program Files\Tesseract-OCR/tesseract'
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(image)
#print the text line by line
print(text[:-1])
