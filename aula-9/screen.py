
import pyautogui
import numpy as np
import cv2

def fullScreenCapture():
    capture = pyautogui.screenshot()
    captureArray = np.array(capture)
    return captureArray

def partialScreenCapture(top, left, width, height):
    capture = pyautogui.screenshot(region=(left, top, width, height))
    captureArray = np.array(capture)
    return captureArray

def grayScaleImage(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale

def invertColor(image):
    inverted = cv2.bitwise_not(image)
    return inverted