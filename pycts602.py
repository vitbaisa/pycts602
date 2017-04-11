#!/usr/bin/env python

import minimalmodbus

client = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
data = client.read_register(0, 1) # Registernumber, number of decimals
print data
