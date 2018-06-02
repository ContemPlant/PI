import struct


def parse_from_sensor_bytes(sensor_bytes: bytes) -> tuple:
    """
    Receives bytes and parses them according to protocol
    :param sensor_bytes: bytes received
    :return: tuple representation
    """
    return struct.unpack_from('=BHLBffff', sensor_bytes)


def parse_to_load_plant_bytes(plant_data: dict) -> bytes:
    """
    Parses plant object into bytes according to loadPlant protocol
    :param plant_data: all attributes that make out a plant
    :return: byte representation
    """
    return struct.pack('=Bffffffff', *load_plant_object_to_tuple(plant_data))


def load_plant_object_to_tuple(load_plant_object: dict) -> tuple:
    """
    Generates tuple out of object according to loadPlant protocol

    :param load_plant_object: dict of plant attributes
    :return: tuple representation
    """
    return (
        1,
        load_plant_object['temperature_opt'],
        load_plant_object['temperature_weight'],
        load_plant_object['humidity_opt'],
        load_plant_object['humidity_weight'],
        load_plant_object['radiation_opt'],
        load_plant_object['radiation_weight'],
        load_plant_object['loudness_opt'],
        load_plant_object['loudness_weight'],
    )


def sensor_tuple_to_object(sensor_type, value, time_stamp, ardu_id) -> dict:
    """
    # Sensor values to dict parsing

    :param sensor_type: the type of this sensor
    :param value: measured value
    :param time_stamp: when was this value recorded
    :param ardu_id: which ardu recorded the date
    :return: object representation
    """
    return {
        "type": sensor_type,
        "value": value,
        "timestamp": f'"{time_stamp}"',
        "arduId": f'"{ardu_id}"'
    }

