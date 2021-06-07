import PicoMotorDriver
import time

motor_board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

while True:
        for direction in directions:
            for stepcount in range(50):
                motor_board.step(direction,8)
            time.sleep(0.1)
                

