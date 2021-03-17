from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import brickpi3  # import the BrickPi3 drivers
import time

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

speed = 0

# Set the motor speed for all four motors
#BP.set_motor_power(BP.PORT_B, 60)
BP.set_motor_power(BP.PORT_C, -60)
BP.set_motor_power(BP.PORT_B, 60)
time.sleep(3)
BP.set_motor_power(BP.PORT_B | BP.PORT_C, -60)
time.sleep(5)
BP.set_motor_power(BP.PORT_B | BP.PORT_C, 0)

#BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_GYRO_DPS)
#time.sleep(5)

#try:
#    while(True):
 #      gs = BP.get_sensor(BP.PORT_3) 
 #      sleep(1)
 #      print("sensor reads " + str(gs))
#except KeyboardInterrupt:
#    print("all done")

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
