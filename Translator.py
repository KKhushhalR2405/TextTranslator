from googletrans import Translator
import cv2
import pytesseract

def trans(word):
    translator=Translator(service_urls=['translate.google.com'])
    translation1=translator.translate(word,dest="hi")
    return translation1.text


custom_config = r'--oem 3 --psm 6'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


####--------Main--------####

img = cv2.imread("img3.jpg")  #change image path accordingly
text=pytesseract.image_to_string(img)
print(text)
print(trans(text))



