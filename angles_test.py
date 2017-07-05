# uArm Swift Pro - Jenga builting
# Created by: Monopatis Dimitrios - monopatis+git@gmail.com
# V0.1 - July 2017 - Still under development

import uArmRobot
import time
import signal
import sys

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        myRobot.pump(False)
        myRobot.goto(104,3,42,6000)
        time.sleep(1)
        myRobot.disconnect()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#Configure Serial Port
# serialport = "com3"          # for windows
serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm
myRobot = uArmRobot.robot(serialport)
myRobot.debug = True   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)
myRobot.goto(200,0,100,6000)
myRobot.get_angle(0)
myRobot.set_angle(0,40)
myRobot.set_angle(3,40)
myRobot.set_angle(3,40)
myRobot.set_angle(3,40)
myRobot.get_angle(0)
end = input("End!")
myRobot.goto(120,120,100,6000)
# time.sleep(1.5)
myRobot.goto(101.18,20,40,6000)
#Disconnect serial connection
myRobot.disconnect()
