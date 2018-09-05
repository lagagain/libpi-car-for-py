#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# test_hcsr04.py
# Measure the distance between HC-SR04 and nearest wall or solid object.
#
# Author : sosorry
# Date   : 09/13/2014

import RPi.GPIO as GPIO
import time

v = 343		# (331 + 0.6*20)

GPIO.setmode(GPIO.BOARD)

hcsr04_trigger_pin = {'L':29, 'F':32, 'R':38, 'B':7}
hcsr04_echo_pin    = {'L':31, 'F':36, 'R':40, 'B':11}

def pin_setup():
    for name, pin in hcsr04_trigger_pin.iteritems():
        GPIO.setup(pin,  GPIO.OUT, initial=GPIO.LOW)

    for name, pin in hcsr04_echo_pin.iteritems():
        GPIO.setup(pin,  GPIO.IN)

def measure_distance(trigger_pin, echo_pin) :
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)	# 10uS 
    GPIO.output(trigger_pin, GPIO.LOW)
    pulse_start = time.time()

    while GPIO.input(echo_pin) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t * v
    d = d/2

    return round(d*100, 2)



try :
    pin_setup()

    while True:
        print "============================"
        print 'L:', measure_distance(hcsr04_trigger_pin['L'], hcsr04_echo_pin['L'])
        print 'F:', measure_distance(hcsr04_trigger_pin['F'], hcsr04_echo_pin['F'])
        print 'R:', measure_distance(hcsr04_trigger_pin['R'], hcsr04_echo_pin['R'])
        print 'B:', measure_distance(hcsr04_trigger_pin['B'], hcsr04_echo_pin['B'])

        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
