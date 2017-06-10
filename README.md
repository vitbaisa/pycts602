# Python API for Nilan CTS602 ModBus

Datasheet for registers taken from `github/roggmaeh/nilan-openhab`

[CTS602 documentation](http://www.nilan.dk/Admin/Public/Download.aspx?File=Files%2FFiler%2FDownload%2FFrench%2FDocumentation%2FGuide+de+montage%2FModbus+CTS+602%2FMODBUS_CTS-602_2.16-2.19_Installation-and-user-guide.pdf)

Another nice repository: `github/nickma82/nilan_communication_bringup`

## Protocol [Modbus (RTU mode)](http://www.modbus.org/specs.php)

Property | Value
---------|------
Node address|Default 30, Address is selectable between 1 and 247|
Device type CTS 602 is a Modbus slave|
Baud rate|19.200|
Databits|8|
Stopbits|1|
Parity|Even|
Packet size|Max. 255 bytes|

_The communication speed and parameter can not be changed._

## Modbus functions

Currently only holding and input registers are supported.

Function|Name|Description
--------|----|-----------
03|Read Holding Registers|Read one or more holding registers|
04|Read Input Registers|Read one or more input registers|
16|Preset Multiple Registers|Write one or more holding registers|
