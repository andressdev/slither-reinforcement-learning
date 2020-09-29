import slither_api
import pyautogui

def getMousePosition():
    return pyautogui.position()

print(getMousePosition())