# This code is a running Concurrently
# For convention Acuvim address 16384 is addressed starting from address 1 in this code see address mapping

## Imports

import time
from ModbusRequest import getRequest
from ModbusRead import readSensor
import threading

## This function setups modbus reading from the sensor
# def SetupSerialReading():
#         instrument = minimalmodbus.Instrument('COM7', 1)  # port name, slave address (in decimal)
#         instrument.serial.baudrate = 9600         # Baud
#         instrument.serial.bytesize = 8
#         instrument.serial.parity   = serial.PARITY_NONE
#         instrument.serial.stopbits = 1
#         instrument.serial.timeout  = 0.2          # seconds
#         instrument.mode = minimalmodbus.MODE_RTU
#         return instrument

# ## Start sensor reading serial
# instrument= SetupSerialReading()

modbusRequest= threading.Thread(target=getRequest)
modbusRead= threading.Thread(target= readSensor)

modbusRead.setDaemon(True)
modbusRequest.setDaemon(True)
modbusRequest.start()
modbusRead.start()

while (True):
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("breaking")
        break
