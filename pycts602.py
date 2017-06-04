#!/usr/bin/env python
#coding=utf-8

__author__ = 'Vit Baisa'

import time
import serial
import struct
import minimalmodbus
from cts602_registers import registers

class CTS602(minimalmodbus.Instrument):

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
    m.debug = True
    for o in registers:
        print o['address'], o['name'], o['description']
        try:
            print 'Value1:', m.read_register(int(o['address']))
        except ValueError, e:
            try:
                time.sleep(1)
                print 'Value2:', m.read_register(int(o['address']), signed=True)
            except ValueError:
                print 'Value3: ???'
        time.sleep(1)
        print '--'*10
