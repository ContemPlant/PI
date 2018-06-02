import unittest
import struct
from src.parsing import parse_from_sensor_bytes, sensor_tuple_to_object


class TestParsing(unittest.TestCase):

    def test_parse_bytes(self):
        protocol_format = '=BHLBffff'

        # Data vector
        x = (1, 0, 1, 0, 27.5, 40, 300, 20)
        flags, aid, timestamp, compression, temp, hum, rad, loud = x

        # Convert to bytes
        bytes = struct.pack(protocol_format, flags, aid, timestamp, compression,
                            temp, hum, rad, loud)

        self.assertEqual(struct.calcsize(protocol_format), 24)
        self.assertEqual(parse_from_sensor_bytes(bytes), x)

    def test_sensor_to_obj(self):
        type, value, timestamp, arduId = 'X', '1', 'now', 'ardu1'
        obj = sensor_tuple_to_object(type, value, timestamp, arduId)
        self.assertEqual(obj['type'], type)
        self.assertEqual(obj['value'], value)
        self.assertEqual(obj['timestamp'], f'"{timestamp}"')
        self.assertEqual(obj['arduId'], f'"{arduId}"')


if __name__ == '__main__':
    unittest.main()
