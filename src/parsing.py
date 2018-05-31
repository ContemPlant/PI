import struct


# Receives bytes and parses them according to protocol
def parseFromSensorBytes(bytes):
    return struct.unpack_from('=BHLBffff', bytes)


def parseToLoadPlantBytes(plantDataTuple):
    flag, t_o, t_w, h_o, h_w, r_o, r_w, l_o, l_w = plantDataTuple

    return struct.pack('=Bffffffff', flag, t_o, t_w, h_o, h_w, r_o, r_w, l_o, l_w)


def loadPlantObjectToTuple(loadPlantObject):
    return (
        1,
        loadPlantObject['temperature_opt'],
        loadPlantObject['temperature_weight'],
        loadPlantObject['humidity_opt'],
        loadPlantObject['humidity_weight'],
        loadPlantObject['radiation_opt'],
        loadPlantObject['radiation_weight'],
        loadPlantObject['loudness_opt'],
        loadPlantObject['loudness_weight'],
    )
