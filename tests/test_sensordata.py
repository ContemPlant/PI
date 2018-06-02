import unittest
from tests.utils import generatorTester
from src.sensorData import xbee_message_receive


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
        generatorTester(xbee_message_receive(device), msgs)


if __name__ == '__main__':
    unittest.main()