#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class Relay:
    """
       The relaybord is controlled by logic levels (1 wire per relay).
       Logic level low => Relay closed (for NO mode)
       Logic level high => Relay opened (for NO mode)
    """

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def relay_close(self):
        """ Close the relay (for NO wiring)
        """
        GPIO.output(self.pin, False)
        
    def relay_open(self):
        """ Open the relay (for NO wiring)
        """
        GPIO.output(self.pin, True)

    def pulse_no(self, time_ms = 1000):
        """ Make the relay closed (for NO wiring) for <time_ms> ms and then make it open
            @param time_ms : time of on status
        """
        self.relay_close()
        time.sleep(time_ms / 1000.)
        self.relay_open()
       
if __name__ == "__main__":
    r = Relay("relay on gpio 11", 11)
    r.pulse_no()
