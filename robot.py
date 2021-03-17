from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import time  # import the time library for the sleep function

import navigator
import sys, tty
import termios


def _getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


nav = navigator.Navigator()

try:
    msg = ''
    while msg != 'q':
        msg = _getch()
        if msg == 'e':
            nav.send_message('forward')
        elif msg == 'd':
            nav.send_message('backward')
        elif msg == 's':
            nav.send_message('left')
        elif msg == 'f':
            nav.send_message('right')
except KeyboardInterrupt:
    print("All done")
    
nav.quit()

# import brickpi3  # import the BrickPi3 drivers
#
# BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
#
# speed = 0
#
# # Set the motor speed for all four motors
# BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, speed)
# time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
#
#
# def forward(rate, duration):
#     BP.set_motor_power(BP.PORT_A + BP.PORT_D, -rate)
#     time.sleep(duration)
#
#
# def backward(rate, duration):
#     BP.set_motor_power(BP.PORT_A + BP.PORT_D, rate)
#     time.sleep(duration)
#
#
# def stop():
#     BP.set_motor_power(BP.PORT_A + BP.PORT_D, 0)
#
#
# def turn_right(rate, duration):
#     BP.set_motor_power(BP.PORT_A, rate)
#     BP.set_motor_power(BP.PORT_D, -rate)
#     time.sleep(duration)
#
#
# def turn_left(rate, duration):
#     BP.set_motor_power(BP.PORT_A, -rate)
#     BP.set_motor_power(BP.PORT_D, rate)
#     time.sleep(duration)
#
#
# forward(80, 10)
# turn_right(100, 5)
# backward(100, 5)
#
# stop()
