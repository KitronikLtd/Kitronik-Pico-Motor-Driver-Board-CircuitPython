#SimgleMotorTest.py
# test code that ramps each motor individually form 0-100-0 then changes direction and does it again then steps onto next motor.
import PicoMotorDriver
import time


motor_board = PicoMotorDriver.KitronikPicoMotor()
directions = ["f","r"]

while True:
    
    for motor in range(2):
        for direction in directions:
            for speed in range(100):
                motor_board.motorOn(motor+1, direction, speed)
                time.sleep(0.01) #ramp speed over 10x100ms => approx 1 second.
            time.sleep(1)
            for speed in range(100):
                motor_board.motorOn(motor+1, direction, 100-speed) #ramp down
                time.sleep(0.01) #ramp speed over 10x100ms => approx 1 second.
            time.sleep(1)
        time.sleep(0.5)#pause between motors 
    
