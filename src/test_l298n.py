#!/usr/bin/python 
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# test_l298n.py
# control car with argument [w=forward/a=left/s=backward/d=right]
# usage: sudo python move_car.py [w/a/s/d]
#
# Author : sosorry
# Date   : 08/01/2015

import RPi.GPIO as GPIO
import time
import readchar


Motor_R1_Pin = 16
Motor_R2_Pin = 18
Motor_L1_Pin = 13
Motor_L2_Pin = 15
t = 0.2


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)


def stop():
    GPIO.output(Motor_R1_Pin, GPIO.LOW)
    GPIO.output(Motor_R2_Pin, GPIO.LOW)
    GPIO.output(Motor_L1_Pin, GPIO.LOW)
    GPIO.output(Motor_L2_Pin, GPIO.LOW)


def forward():
    GPIO.output(Motor_R1_Pin, GPIO.HIGH)
    GPIO.output(Motor_R2_Pin, GPIO.LOW)
    GPIO.output(Motor_L1_Pin, GPIO.HIGH)
    GPIO.output(Motor_L2_Pin, GPIO.LOW)
    time.sleep(t)
    stop()


def backward():
    GPIO.output(Motor_R1_Pin, GPIO.LOW)
    GPIO.output(Motor_R2_Pin, GPIO.HIGH)
    GPIO.output(Motor_L1_Pin, GPIO.LOW)
    GPIO.output(Motor_L2_Pin, GPIO.HIGH)
    time.sleep(t)
    stop()


def turnRight():
    GPIO.output(Motor_R1_Pin, GPIO.HIGH)
    GPIO.output(Motor_R2_Pin, GPIO.LOW)
    GPIO.output(Motor_L1_Pin, GPIO.LOW)
    GPIO.output(Motor_L2_Pin, GPIO.LOW)
    time.sleep(t)
    stop()

def turnLeft():
    GPIO.output(Motor_R1_Pin, GPIO.LOW)
    GPIO.output(Motor_R2_Pin, GPIO.LOW)
    GPIO.output(Motor_L1_Pin, GPIO.HIGH)
    GPIO.output(Motor_L2_Pin, GPIO.LOW)
    time.sleep(t)
    stop()


if __name__ == "__main__":

    print "Press 'q' to quit..."

    while True:
        ch = readchar.readkey()

        if ch == 'w':
            forward()

        elif ch == 's':
            backward()

        elif ch == 'd':
            turnRight()

        elif ch == 'a':
            turnLeft()

        elif ch == 'q':
            print "\nQuit"
            GPIO.cleanup()
            quit()

