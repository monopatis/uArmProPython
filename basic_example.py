# uArm Swift Pro - Python Library Example
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.1 - June 2017 - Still under development

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
myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)
# Move robot, command will complete when motion is completed
myRobot.goto(200,0,100,6000)
# Turn on the pump
# myRobot.pump(True)
# Send move command, but continue program
myRobot.async_goto(200,150,250,3000)
while myRobot.moving:
    print ("Waiting to complete move")
    time.sleep(1.5)
#Turn off the pump
# myRobot.pump(False)
# Send move command, but continue program
myRobot.async_goto(200,0,100,6000)
while myRobot.moving:
    print ("Waiting to complete move")
    time.sleep(1.55)
time.sleep(1.5)
myRobot.goto(104,3,42,6000)
#Disconnect serial connection
myRobot.disconnect()
