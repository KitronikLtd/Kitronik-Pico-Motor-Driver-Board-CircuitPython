import PicoMotorDriver
import board
from digitalio import DigitalInOut, Direction, Pull

motor_board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

Input1 = DigitalInOut(board.GP0)
Input1.direction = Direction.INPUT
Input1.pull = Pull.DOWN

Input2 = DigitalInOut(board.GP1)
Input2.direction = Direction.INPUT
Input2.pull = Pull.DOWN

Input3 = DigitalInOut(board.GP26)
Input3.direction = Direction.INPUT
Input3.pull = Pull.UP

Input4 = DigitalInOut(board.GP27)
Input4.direction = Direction.INPUT
Input4.pull = Pull.UP


# Switch out Input 1 and 2 for Input 3 and 4 as part of testing

while True:
    if(Input1.value):
        direction1 = "f"
    else:
        direction1 = "r"
    if(Input2.value):
        direction2 = "f"
    else:
        direction2 = "r"
    motor_board.motorOn(1, direction1, 75)
    motor_board.motorOn(2, direction2, 75)

