import pytesseract
import slither_api
import screen

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def read(image):
    text = pytesseract.image_to_string(image)
    return text

def readScreen(top, left, width, height):
    capture = screen.partialScreenCapture(top, left, width, height)
    text = read(capture)
    return text
