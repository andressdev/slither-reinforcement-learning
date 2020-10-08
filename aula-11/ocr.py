import pytesseract
import slither_api
import screen

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def read(image, invert):
    grayscale = screen.grayScaleImage(image)
    if(invert):
        grayscale = screen.invertColor(grayscale)
    text = pytesseract.image_to_string(grayscale)
    return text

def readScreen(top, left, width, height, invert):
    capture = screen.partialScreenCapture(top, left, width, height)
    text = read(capture, invert)
    return text
