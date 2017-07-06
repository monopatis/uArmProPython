# uArm Swift Pro - Jenga builting
# Created by: Monopatis Dimitrios - monopatis+git@gmail.com
# Video can find here: https://www.youtube-nocookie.com/embed/DTmQRKxS4So?rel=0
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
myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)
myRobot.goto(200,0,100,6000)
z=10.69+20
down=-27.558
for block in range(0,3):
    x=145.69
    y=0
    for num in range(0,3):
        myRobot.goto(200,0,100,6000)
        myRobot.set_angle(3,58)
        myRobot.goto(300,0,100,6000)
        myRobot.move(0,0,down,2000)
        # Turn on the pump
        myRobot.pump(True)
        myRobot.move(0,0,27,2000)
        myRobot.goto(200,0,100,6000)
        myRobot.goto(x,y,z,6000)
        myRobot.move(0,0,-20,2000)
        #Turn off the pump
        myRobot.pump(False)
        myRobot.move(0,0,7,2000)
        time.sleep(1.5)
        x=x+27.5
    x=x-2*27.5-6.5
    y=-27.5
    z=z+15.09
    angle=143
    for num in range(0,3):
        myRobot.goto(200,0,100,6000)
        myRobot.set_angle(3,58)
        myRobot.goto(300,0,100,6000)
        myRobot.move(0,0,down,2000)
        # Turn on the pump
        myRobot.pump(True)
        myRobot.move(0,0,27,2000)
        myRobot.goto(200,0,100,6000)
        myRobot.set_angle(3,angle)
        myRobot.goto(x,y,z,6000)
        myRobot.move(0,0,-20,2000)
        myRobot.pump(False)
        myRobot.move(0,0,7,2000)
        time.sleep(1.5)
        y=y+28.5
        angle=angle+9
    z=z+15.09
myRobot.goto(120,120,100,6000)
# time.sleep(1.5)
myRobot.goto(101.18,20,40,6000)
#Disconnect serial connection
myRobot.disconnect()
