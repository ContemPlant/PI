from parsing import parse_from_sensor_bytes


def xbee_message_receive(device):
    """
    # generator for xbee messages from given device

    :param device: the device from which to read
    """
    while True:
        # TODO Check that port is really open
        # if(not device.__get_serial_port()._isOpen):
        #    pass
        message = device.read_data()
        if message is not None:
            print("Got message")
            yield message


def sensor_dates(device):
    """
    generator for parsed sensor dates

    :param device: the device from which to read
    """
    for message in xbee_message_receive(device):
        # address = xbee_message.remote_device.get_16bit_addr()
        data = message.data
        yield parse_from_sensor_bytes(data)
