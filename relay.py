#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


class Relay:
    """
       The relaybord is controlled by logic levels (1 wire per relay).
       Logic level low => Relay closed (for NC mode)
       Logic level high => Relay opened (for NC mode)

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        """ Set the relay on (if NC) 
        """
        GPIO.output(self.pin, False)
        
    def off(self):
        """ Set the relay off (if NC) 
        """
        GPIO.output(self.pin, True)

    def pulse(self, time_ms = 1000):
        """ Make the relay on for <time_ms> ms and then make it off. 
            @param time_ms : time of on status
        """
        self.on()
        time.sleep(time_ms / 1000.)
        self.off()
       
if __name__ == "__main__":
    r = Relay("relay on gpio 11", 11)
    r.pulse()
    #l.on()
    #time.sleep(2)
    #l.off()
    #time.sleep(2)
    #l.on()
    #time.sleep(2)
    #l.off()
