import serial
import struct
from digi.xbee.devices import XBeeDevice

serialPort = '/dev/tty.usbserial-DN02MLF3'


def parseBytes(bytes):
    try:
        return struct.unpack_from('=BBBLBBfff', bytes)
    except struct.error:
        return -1


device = XBeeDevice(serialPort, 9600)
device.open()


def messageReceive():
    # Instantiate an XBee device object.

    while True:
        message = device.read_data()
        if message is not None:
            yield message


def sensorDates():
    for message in messageReceive():
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parseBytes(data)
