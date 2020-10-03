import slither_api
import pyautogui
from time import sleep

def getMousePosition():
    return pyautogui.position()

print('Get position 1')
position1 = getMousePosition()
print('Go to position 2')
sleep(5)
position2 = getMousePosition()
width = position2[0] - position1[0]
heigth = position2[1] - position1[1]
print('top:', position1[1], 'left: ', position1[0], 'width: ', width, 'height: ', heigth)