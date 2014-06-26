#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import traceback
import binascii
import logging


class RfidSerialMFRC522:

    def __init__(self, device):
        """ Open the serial port and configure the Rfid reader
        """
        # Open the RFID reader
        try:
            self.rfid_reader = serial.Serial(device)
        except:
            logging.error("Error while opening Rfid reader : {0}".format(traceback.format_exc()))
            raise

        # Configure the RFID reader 
        # command     # explain
        ########################################################################
        # 0x01        #Automatically search cards
        # 0x02        #Automatically read the card serial number.
        # 0x03        #Card serial number will be automatically stored in the EEPROM
        # 0x04        #Automatically determine whether the card is in authorization list
        # 0x05        #Automatically find and remove the card in authorization list

        # here we just want to read the cards id :
        # the auth process will be done somewhere else
        self.rfid_reader.write("\x02")
        # flush 
        #self.rfid_reader.flush()

    def read(self, callback):
        """ Listen for the rfid reader
            When a card id is detected, call the callback with the id as parameter
            @param callback : function to call when a card is detected
        """
        logging.debug("Start to listen to the rfid reader")
        while True:
            try:
                card_bin = self.rfid_reader.read(4)
                # flush the input in case there were too much data waiting....
                self.rfid_reader.flushInput()
                card_txt = binascii.hexlify(card_bin)
                logging.debug("Rfid item detected : {0}".format(card_txt))
                callback(card_txt)
            except (KeyboardInterrupt, SystemExit):
                logging.error("Keyboard (or system) interrupt : stop listening to the rfid reader!")
                self.rfid_reader.close()
                raise


def my_cb(data):
    logging.debug("DATA > {0}".format(data))

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    R = RfidSerialMFRC522("/dev/ttyAMA0")
    R.read(my_cb)
