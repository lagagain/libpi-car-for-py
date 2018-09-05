#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# test_tracking.py
# Response when tracking module is triggered
#
# Author : sosorry
# Date   : 02/11/2016

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
WAIT_TIME = 200
tracking_pin = {'L':33, 'F':35, 'R':37}

def pin_setup():
    for name, pin in tracking_pin.iteritems():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def mycallback(channel):
    print(str(channel) + ' triggered @ ' +  str(time.ctime()))



if __name__ == "__main__":
     try:
         pin_setup()

         for name, pin in tracking_pin.iteritems():
             GPIO.add_event_detect(pin, GPIO.RISING, callback=mycallback, bouncetime=WAIT_TIME)

         while True:
             time.sleep(10)

     except KeyboardInterrupt:
         print("Exception: KeyboardInterrupt")

     finally:
         GPIO.cleanup()
