def sendData(node_id, payload, device):

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
