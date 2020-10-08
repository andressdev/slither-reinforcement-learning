import slither_api
import cv2
import numpy as np


screen = slither_api.returnGameScreen(956, 515)
print(screen.shape)
cv2.imshow("test", screen)
cv2.waitKey(0)