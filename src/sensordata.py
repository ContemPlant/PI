import serial
import struct
from digi.xbee.devices import XBeeDevice, Raw802Device
from digi.xbee.exception import TimeoutException

serialPort = '/dev/tty.usbserial-DN02MM7G'
baudRate = 9600


# Receives bytes and parses them according to protocol
def parseBytes(bytes):
    try:
        return struct.unpack_from('=BBBLBBfff', bytes)
    except struct.error:
        return -1


# Sensor values to object parsing
def sensorToObj(type, value, timestamp, arduId):
    return {
        "type": type,
        "value": value,
        "timestamp": f'"{timestamp}"',
        "arduId": f'"{arduId}"'
    }


# generator for xbee messages from given device
def messageReceive(device):

    while True:
        # TODO Check that port is really open
        # if(not device.__get_serial_port()._isOpen):
        #    pass
        message = device.read_data()
        if message is not None:
            yield message


# generator for parsed sensor dates
def sensorDates():

    # Instantiate an XBee device object.
    device = Raw802Device(serialPort, baudRate)
    # TODO Fix checksum error
    device.open()

    for message in messageReceive(device):
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parseBytes(data)
