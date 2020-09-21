import slither_api
from time import sleep

print("begin the game")
slither_api.beginGame()

print("moving top")
slither_api.moveTop()

sleep(3)

print("moving down")
slither_api.moveDown()

sleep(3)

print("moving left")
slither_api.moveLeft()

sleep(3)

print("moving right")
slither_api.moveRight()

sleep(3)

print("moving top left")
slither_api.moveTopLeft()

sleep(3)

print("moving top right")
slither_api.moveTopRight()

sleep(3)

print("moving down left")
slither_api.moveDownLeft()

sleep(3)

print("moving down  right")
slither_api.moveDownRight()

sleep(5)
print("test done")