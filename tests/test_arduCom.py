import unittest
from tests.utils import generator_tester
from src.xbeeNetwork.arduCom import \
    xbee_message_receive, \
    send_data


class TestSensorData(unittest.TestCase):

    def test_message_receive(self):
        class MockDevice:
            def __init__(self, messages):
                self.messages = messages

            def read_data(self):
                if len(self.messages) == 0:
                    return 0
                self.messages.pop()

        msgs = ['HEY', 'HO', 'HI']
        device = MockDevice(msgs)
        assert generator_tester(xbee_message_receive(device), msgs) is True

    def test_send_data(self):
        # -------- Mock all the stuff -----------
        class Network:
            def __init__(self, devices):
                self.devices = devices

            def discover_device(self, node_id):
                return self.devices[node_id]

        class MockDevice:
            def __init__(self, messages, network):
                self.messages = messages
                self.network = network

            def receive_data(self, payload):
                self.messages.append(payload)

            def send_data(self, device, payload):
                device.receive_data(payload)

            def get_network(self):
                return self.network

            def get_16bit_addr(self):
                return "i am an address"

        node_id = "A001"
        message = "WTF"

        devices = {node_id: MockDevice([], 0)}
        xbee_network = Network(devices)
        mock_device = MockDevice([], xbee_network)
        # --------------finished mocking --------------

        send_data(node_id, message, mock_device)
        assert devices[node_id].messages == [message]


if __name__ == '__main__':
    unittest.main()
