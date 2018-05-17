import serial
import struct
from digi.xbee.devices import XBeeDevice

serialPort = '/dev/tty.usbserial-DN02MM7G'
baudRate = 9600


# Receives bytes and parses them according to protocol
def parseBytes(bytes):
    try:
        return struct.unpack_from('=BBBLBBfff', bytes)
    except struct.error:
        return -1


# generator for xbee messages from serial port
def messageReceive(port, baud):
    # Instantiate an XBee device object.
    device = XBeeDevice(port, baud)
    # TODO Fix checksum error
    device.open()

    while True:
        # TODO Check that port is really open
        if(not device._is_open):
            pass
        message = device.read_data()
        if message is not None:
            yield message


# generator for parsed sensor dates
def sensorDates():
    for message in messageReceive(serialPort, baudRate):
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parseBytes(data)
