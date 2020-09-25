from pytesseract import image_to_string
import slither_api

def read(image):
    text = image_to_string(image)
    return text