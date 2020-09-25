import slither_api
from time import sleep
import ocr

#capture = slither_api.partialScreenCapture(343, 836, 262, 29)
text = ocr.readScreen(986, 552, 102, 31)
print(text)