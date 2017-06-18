#!/usr/bin/env python
#coding=utf-8

__author__ = 'Vit Baisa'

import time
import serial
import struct
import minimalmodbus
from cts602_registers import registers

class CTS602API(minimalmodbus.Instrument):

    def __init__(self, portname, slaveaddr=30):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddr)
        self.serial.parity = serial.PARITY_EVEN
        self.serial.timeout = 1.0
        self.format = 'bbbhh'
        self.reg2addr = dict([(x['name'], x['address']) for x in registers])

    def getExtTemp(self):
        return self.read_register(self.reg2addr['Nilan_Input_T1_Intake'], numberOfDecimals=2)

    def getAddrData(self, address=000):
        assert type(address) == type(0)
        return self.read_register(address)


if __name__ == '__main__':
    m = CTS602('/dev/ttyUSB0')
    #m.debug = True
    for o in registers:
        if o['type'] == 'Input':
            v = m.read_register(o['address'], functioncode=4)
        elif o['type'] == 'Holding':
            v = m.read_register(o['address'])
        print '%c\t%d\t%s\t%s\t%s' % (o['type'][0], o['address'], str(v), o['name'], o['description'])
        time.sleep(1)
