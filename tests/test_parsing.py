import unittest
import struct
from src.parsing import \
    parse_from_sensor_bytes, \
    sensor_tuple_to_object, \
    load_plant_object_to_tuple, \
    parse_to_load_plant_bytes


class TestParsing(unittest.TestCase):

    def test_parse_from_sensor_bytes(self):
        protocol_format = '=BHLBffff'

        # Data vector
        sensor_tuple = (1, 0, 1, 0, 27.5, 40, 300, 20)

        # Convert to bytes
        bytes = struct.pack(protocol_format, *sensor_tuple)

        self.assertEqual(struct.calcsize(protocol_format), 24)
        self.assertEqual(parse_from_sensor_bytes(bytes), sensor_tuple)

    def test_load_plant_object_to_tuple(self):
        load_plant_object = {
            'temperature_opt': 20,
            'temperature_weight': 1.0,
            'humidity_opt': 400,
            'humidity_weight': 1.0,
            'radiation_opt': 1337,
            'radiation_weight': 0.03,
            'loudness_opt': 4.6,
            'loudness_weight': 100.0,
        }
        expected_tuple = (1, 20, 1.0, 400, 1.0, 1337, 0.03, 4.6, 100.0)
        assert load_plant_object_to_tuple(load_plant_object) == expected_tuple

    def test_parse_to_load_plant_bytes(self):
        load_plant_object = {
            'temperature_opt': 20,
            'temperature_weight': 1.0,
            'humidity_opt': 400,
            'humidity_weight': 1.0,
            'radiation_opt': 1337,
            'radiation_weight': 0.03,
            'loudness_opt': 4.6,
            'loudness_weight': 100.0,
        }
        expected_bytes = bytes(b'\x01\x00\x00\xa0A\x00\x00\x80?\x00\x00\xc8C\x00\x00\x80?\x00 '
                               b'\xa7D\x8f\xc2\xf5<33\x93@\x00\x00\xc8B')
        assert parse_to_load_plant_bytes(load_plant_object) == expected_bytes

    def test_sensor_tuple_to_object(self):
        type, value, timestamp, ardu_id = 'X', '1', 'now', 'ardu1'
        obj = sensor_tuple_to_object(type, value, timestamp, ardu_id)
        self.assertEqual(obj['type'], type)
        self.assertEqual(obj['value'], value)
        self.assertEqual(obj['timestamp'], f'"{timestamp}"')
        self.assertEqual(obj['arduId'], f'"{ardu_id}"')


if __name__ == '__main__':
    unittest.main()
