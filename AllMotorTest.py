#AllMotorTest.py
# test code that ramps each motor 0-100-0 then changes direction and does it again.
#all motors run at once, but with staggered timings

import PicoMotorDriver
import time

motor_board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

while True:
    for direction in directions:
        for speed in range(0,25):
            motor_board.motorOn(1, direction, speed)
            motor_board.motorOn(2, direction, 25-speed)
            time.sleep(0.1) #ramp speed over 25x100ms => approx 2.5 second.
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 25+speed)
            motor_board.motorOn(2, direction, speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 50+speed)
            motor_board.motorOn(2, direction, 25+speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 75+speed)
            motor_board.motorOn(2, direction, 50+speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 100-speed)
            motor_board.motorOn(2, direction, 75+speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 75-speed)
            motor_board.motorOn(2, direction, 100-speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 50-speed)
            motor_board.motorOn(2, direction, 75-speed)
            time.sleep(0.1)
        for speed in range(0,25):
            motor_board.motorOn(1, direction, 25-speed)
            motor_board.motorOn(2, direction, 50-speed)
            time.sleep(0.1)


