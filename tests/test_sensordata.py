import unittest
import sys
import struct
from tests.utils import generatorTester
from src.sensordata import parseBytes, sensorToObj, messageReceive


class TestSensorData(unittest.TestCase):

    def test_parse_bytes(self):
        # Data vector
        x = (1, 0, 1, 100, 1, 0, 4.0, 3.0, 2.0)
        flags, pid, aid, timestamp, phealth, psize, temp, hum, rad = x

        # Convert to bytes
        bytes = struct.pack('=BBBLBBfff', flags, pid, aid, timestamp,
                            phealth, psize, temp, hum, rad)

        self.assertEqual(parseBytes(bytes), x)

    def test_sensor_to_obj(self):
        type, value, timestamp, arduId = 'X', '1', 'now', 'ardu1'
        obj = sensorToObj(type, value, timestamp, arduId)
        self.assertEqual(obj['type'], type)
        self.assertEqual(obj['value'], value)
        self.assertEqual(obj['timestamp'], f'"{timestamp}"')
        self.assertEqual(obj['arduId'], f'"{arduId}"')

    def test_message_receive(self):
        class mockDevice:
            def __init__(self, messages):
                self.messages = messages

            def read_data(self):
                if len(self.messages) == 0:
                    return 0
                self.messages.pop()

        msgs = ['HEY', 'HO', 'HI']
        device = mockDevice(msgs)
        generatorTester(messageReceive(device), msgs)


if __name__ == '__main__':
    unittest.main()
