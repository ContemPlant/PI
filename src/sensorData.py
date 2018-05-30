import serial
from digi.xbee.devices import XBeeDevice, Raw802Device
from digi.xbee.exception import TimeoutException
from parsing import parseFromSensorBytes


serialPort = '/dev/tty.usbserial-DN02MM7G'
baudRate = 9600


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
    device.open()

    for message in messageReceive(device):
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parseFromSensorBytes(data)
