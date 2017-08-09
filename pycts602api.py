#!/usr/bin/env python
#coding=utf-8

__author__ = 'Vit Baisa'

import time
import serial
import struct
import minimalmodbus
from cts602_registers import registers

class CTS602API(minimalmodbus.Instrument):

    def __init__(self, portname='/dev/ttyUSB0', slaveaddr=30):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddr)
        self.registers = registers
        self.serial.parity = serial.PARITY_EVEN
        self.serial.timeout = 1.0
        self.format = 'bbbhh'
        self.reg2addr = dict([(x['name'], x['address']) for x in registers])

    def normalize(self, record, value):
        if record.get('values',False):
            return record['values'].get(value, value)
        ru = record['unit']
        if ru in ['ascii', 'text']: # 2 chars
            return value
        elif ru == '%':
            return round(value / 100.0, 1)
        elif ru == '\xc2\xb0C':
            return round(value / 100.0, 1)
        elif ru == 'Step':
            # TODO?
            return value
        elif ru == 'min': # minutes
            return value

    def getVP18KWTRealtimeData(self):
        o = []
        for i in self.registers:
            new_i = dict(i)
            fc = i['type'] == 'Input' and 4 or 3
            v = self.read_register(i['address'], functioncode=fc)
            new_i['raw'] = v
            new_i['value'] = self.normalize(i, v)
            o.append(new_i)
        return o


if __name__ == '__main__':
    m = CTS602API('/dev/ttyUSB0')
    for o in m.registers:
        if o['type'] == 'Input':
            v = m.read_register(o['address'], functioncode=4)
        elif o['type'] == 'Holding':
            v = m.read_register(o['address'])
        # write out only VP-supported registers
        if not 'VP' in o['devices'] and o['devices'] != 'All plants':
            continue
        t = o.get('values', False) and o['values'].get(v, '???') or ''
        print '%c\t%d\t%s\t%s\t%s\t%s' % (o['type'][0], o['address'], str(v),
                t, o['name'], o['description'])
