from digi.xbee.devices import Raw802Device
from parsing import parseToLoadPlantBytes

# Tthe serial port where your local module is connected to.
PORT = '/dev/tty.usbserial-DN02MM7G'
# the baud rate of your local module.
BAUD_RATE = 9600


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


# Playground ################
flag = 0
temp_opt = 20.0
temp_weight = 1.0
hum_opt = 124.3
hum_weight = 0.6
rad_opt = 400.52
rad_weight = 0.4
loud_opt = 2000.0
loud_weight = 1.0

tup = (flag, temp_opt, temp_weight, hum_opt, hum_weight,
       rad_opt, rad_weight, loud_opt, loud_weight)

dem_bytes = parseToLoadPlantBytes(tup)

send_data("A1", dem_bytes)
