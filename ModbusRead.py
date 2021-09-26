from AddressMapping import getOriginalAddress
import minimalmodbus
import serial
from AddressMapping import getDataLength, setLowerByte, setHigherByte
import time


# Used to seperate a number into two bytes
def SeperateBytes(hexValue):
     return divmod(hexValue, 0x100)

# This function setups modbus reading from the sensor
def SetupSerialReading(port):
        instrument = minimalmodbus.Instrument(port, 1)  # port name, slave address (in decimal)
        instrument.serial.baudrate = 9600         # Baud
        instrument.serial.bytesize = 8
        instrument.serial.parity   = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout  = 1         # seconds
        instrument.mode = minimalmodbus.MODE_RTU
        return instrument

def readSensor():
    
    instrument= setupSerial()
    
    while True:
        try:
            readRegisters(instrument)
            time.sleep(45)
        except:
            instrument=setupSerial()
            pass


def readRegisters(instrument):
    for i in range(1, getDataLength()+1):
        high,low = SeperateBytes(instrument.read_register(getOriginalAddress(i))) # Used to seperate the decimal values into two bytes
        setHigherByte(high, i-1)
        setLowerByte(low, i-1)
    print("read the sensor values")
    
def setupSerial():
    try:
        return SetupSerialReading('/dev/ttyUSB2')
    except:
        try:
            return SetupSerialReading('/dev/ttyUSB0')
        except:
            return False




