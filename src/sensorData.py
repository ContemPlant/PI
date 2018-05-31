import serial
from digi.xbee.exception import TimeoutException
from parsing import parseFromSensorBytes

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
            print("Got message")
            yield message


# generator for parsed sensor dates
def sensorDates(device):

    for message in messageReceive(device):
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parseFromSensorBytes(data)
