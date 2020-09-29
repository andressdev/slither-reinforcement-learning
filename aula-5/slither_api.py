
import pyautogui
import numpy as np
import ocr

def beginGame():
    pyautogui.click(x=956, y=515)

def moveTop():
    pyautogui.moveTo(966, 237)

def moveDown():
    pyautogui.moveTo(945, 934)

def moveLeft():
    pyautogui.moveTo(533, 615)

def moveRight():
    pyautogui.moveTo(1294, 618)

def moveTopLeft():
    pyautogui.moveTo(557, 299)

def moveTopRight():
    pyautogui.moveTo(1400, 300)

def moveDownLeft():
    pyautogui.moveTo(581, 959)

def moveDownRight():
    pyautogui.moveTo(1311, 876)

def readFinalScore():
    text = ocr.readScreen(335,819,276,33, True)
    print(text)

def readCurrentScore():
    text = ocr.readScreen(1112,0,147,25, True)
    print(text)