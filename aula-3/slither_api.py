
import pyautogui
import numpy as np

def fullScreenCapture():
    capture = pyautogui.screenshot()
    captureArray = np.array(capture)
    return captureArray

def partialScreenCapture(top, left, width, height):
    capture = pyautogui.screenshot(region=(left, top, width, height))
    captureArray = np.array(capture)
    return captureArray

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