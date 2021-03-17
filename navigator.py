import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers
from threading import Thread, RLock
import sys
import Queue

class Navigator:
    def __init__(self):
        self.messageQueue = Queue.Queue()
        self.BP = brickpi3.BrickPi3()
        self.BP.reset_all()
        time.sleep(1)
        self.BP.set_motor_power(self.BP.PORT_A + self.BP.PORT_B + self.BP.PORT_C + self.BP.PORT_D, 0)
        self.BP.set_sensor_type(self.BP.PORT_1, self.BP.SENSOR_TYPE.NXT_ULTRASONIC)
        self.lock = RLock()
        self.thread = Thread(target=self.process_message)
        self.speed = 50
        self.initial_speed = 30
        self.distance = 0
        self.thread.start()
   
    def get_proximity(self):
        with self.lock:
            return self.distance

    def send_message(self, msg):
        self.messageQueue.put(msg)

    def process_message(self):

            done = False

            while not done:
                try:
                    message = self.messageQueue.get(block=True, timeout=0.50)
                    
                    if message == 'quit':
                        done = True
                    elif message == 'forward':
                        self._forward(self.speed)
                    elif message == 'backward':
                        self._backward(self.speed)
                    elif message == 'right':
                        self._turn_right(self.speed)
                    elif message == 'left':
                        self._turn_left(self.speed)
                    elif message == 'stop':
                        self._stop()
                    elif message == 'distance':
                        self._set_proximity()
                    else:
                        self._stop()
                except Queue.Empty:
                        self._stop()
                except brickpi3.SensorError as error:
                    print(error)

    def quit(self):
        self.messageQueue.put('stop')
        self.messageQueue.put('quit')

    def _forward(self, rate):
        self.BP.set_motor_power(self.BP.PORT_B + self.BP.PORT_C, rate)

    def _backward(self, rate):
        self.BP.set_motor_power(self.BP.PORT_B + self.BP.PORT_C, -rate)

    def _stop(self):
        self.BP.set_motor_power(self.BP.PORT_B + self.BP.PORT_C, 0)

    def _turn_right(self, rate):
        self.BP.set_motor_power(self.BP.PORT_B, rate)
        self.BP.set_motor_power(self.BP.PORT_C, -rate)

    def _turn_left(self, rate):
        self.BP.set_motor_power(self.BP.PORT_B, -rate)
        self.BP.set_motor_power(self.BP.PORT_C, rate)

    def _read_sensor(self):
        return self.BP.get_sensor(self.BP.PORT_1)

    def _set_proximity(self):
        with self.lock:
            self.distance = self._read_sensor()

