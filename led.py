#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import logging


class Led:

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        """ Switch the led on
        """
        logging.debug("Set led '{0}' to on".format(self.name))
        GPIO.output(self.pin, True)
        
    def off(self):
        """ Switch the led off
        """
        logging.debug("Set led '{0}' to off".format(self.name))
        GPIO.output(self.pin, False)

    def blink(self, time_ms = 1000):
        """ Make the led blink 1 time (on/off). The high level will take <time_ms> ms
            @param time_ms : time of both high and low levels
        """
        # TODO : do it as a Thread  ???
        #        or do a second function to do it as a thread ?
        self.on()
        time.sleep(time_ms / 1000.)
        self.off()
       
    def blink_n(self, number = 3, time_ms = 100):
        """ Make the led blink <number> times (on/off) and each low and high level will take <time_ms> ms
            @param number : the number of blinks
            @param time_ms : time of both high and low levels
        """
        # TODO : do it as a Thread 
        for nb in range(0, number):
            self.on()
            time.sleep(time_ms / 1000.)
            self.off()
            time.sleep(time_ms / 1000.)
       
        
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    l = Led("led 7", 7)
    l.blink_n()
    l.blink()
    #l.on()
    #time.sleep(2)
    #l.off()
    #time.sleep(2)
    #l.on()
    #time.sleep(2)
    #l.off()
