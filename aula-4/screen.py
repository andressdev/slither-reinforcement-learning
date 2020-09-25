
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