from src.parsing import parse_from_sensor_bytes


def send_data(node_id, payload, device):
    """
    Sends payload to xbee with given node_id using given device

    :param node_id: Address of receiver
    :param payload: Data (bytes) to send
    :param device: device to send data from
    """
    # Obtain the remote XBee device from the XBee xbeeNetwork.
    xbee_network = device.get_network()
    remote_device = xbee_network.discover_device(node_id)
    if remote_device is None:
        print("Could not find the remote device")
        return

    print("Sending data to %s >> %s..." %
          (remote_device.get_16bit_addr(), payload))

    device.send_data(remote_device, payload)

    print("Success")


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
