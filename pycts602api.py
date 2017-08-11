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
        self.regd = dict([((x['address'], x['type'] == 'Input' and 4 or 3), x)\
                for x in self.registers])
        self.serial.parity = serial.PARITY_EVEN
        self.serial.timeout = 1.0
        self.format = 'bbbhh'
        self.reg2addr = dict([(x['name'], x['address']) for x in registers])

    def turn_off(self):
        self.write_register(1001, 0)
        return 0

    def turn_on(self):
        self.write_register(1001, 1)
        return 1

    def reset_vent(self):
        self.setVentStep(1)
        return 1

    def set_vent_step(self, step=1):
        assert step in [0, 1, 2, 3, 4]
        self.write_register(1003, step)
        return step

    def increase_user_air_temp(self):
        current_temp = self.read_register(1004)
        new_temp = current_temp + 100
        assert new_temp < 2600
        self.write_register(1004, new_temp)
        return new_temp

    def decrease_user_air_temp(self):
        current_temp = self.read_register(1004)
        print current_temp
        new_temp = current_temp - 100
        assert new_temp > 1800
        self.write_register(1004, new_temp)
        return new_temp

    def set_user_temp(self, temp=21):
        assert type(temp) == type(1)
        assert temp < 26 and temp > 18
        self.write_register(1004, temp*100)

    def normalize(self, record, value):
        if record.get('values',False):
            return record['values'].get(value, value)
        ru = record['unit']
        if ru in ['ascii', 'text']: # 2 chars
            ch1 = value % 256
            ch2 = value / 256
            return (ch1 == 223 and '\xc2\xb0' or chr(ch1)) + chr(ch2)
        elif ru == '%':
            return round(value / 100.0, 1)
        elif ru == '\xc2\xb0C':
            return round(value / 100.0, 1)
        elif ru == 'Step':
            # TODO?
            return value
        elif ru == 'min': # minutes
            return value

    def get_realtime_data(self):
        def g(a, fc=3):
            item = self.regd[(a, fc)]
            value = self.read_register(a, functioncode=fc)
            item['raw'] = value
            item['value'] = self.normalize(item, value)
            return item

        return {
            'filter_alarm': g(101, 4),
            'boiling': g(109, 4),
            'board_temp': g(200, 4),
            'intake_temp': g(201, 4),
            'condenser_temp': g(205, 4),
            'evaporator_temp': g(206, 4),
            'inlet_temp': g(207, 4),
            'outdoor_temp': g(208, 4),
            'outlet_temp': g(210, 4),
            'water_top_temp': g(211, 4),
            'water_bottom_temp': g(212, 4),
            'panel_temp': g(215, 4),
            'humidity': g(221, 4),
            'status': g(1002, 4),
            'status_time': g(1003, 4),
            'is_summer': g(1200, 4),
            'display_text': ''.join([g(x, 4)['value'] for x in [2002,2003,2004,2005,2007,2008,2009,2010]]),
            'exhaust_speed': g(200),
            'inlet_speed': g(201),
            'running': g(1001),
            'mode': g(1002),
            'vent_step': g(1003),
            'air_set_temp': g(1004),
            'water_set_temp': g(1701)
        }

    def get_all_realtime_data(self):
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

    m.turn_on()
    exit(0)

    for o in m.registers:
        if o['type'] == 'Input':
            v = m.read_register(o['address'], functioncode=4)
        elif o['type'] == 'Holding':
            v = m.read_register(o['address'])
        # write out only VP-supported registers
        if not 'VP' in o['devices'] and o['devices'] != 'All plants':
            continue
        t = m.normalize(o, v)
        print '%c\t%d\t%s\t%s\t%s\t%s' % (o['type'][0], o['address'], str(v),
                t, o['name'], o['description'])
