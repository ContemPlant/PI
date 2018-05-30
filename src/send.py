from digi.xbee.devices import Raw802Device

# Tthe serial port where your local module is connected to.
PORT = '/dev/tty.usbserial-DN02MM7G'
# the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = 'Hello XBee!'
REMOTE_NODE_ID = 'A1'


def send_data(node_id, payload):
    device = Raw802Device(PORT, BAUD_RATE)

    try:
        device.open()

        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(node_id)
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)

        print("Sending data to %s >> %s..." %
              (remote_device.get_16bit_addr(), payload))

        device.send_data(remote_device, payload)

        print("Success")

    finally:
        if device is not None and device.is_open():
            device.close()
