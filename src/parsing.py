import struct


# Receives bytes and parses them according to protocol
def parseFromSensorBytes(bytes):
    try:
        return struct.unpack_from('=BBBLBBfff', bytes)
    except struct.error:
        return -1


def parseToLoadPlantBytes(plantDataTuple):
    try:
        return struct.pack_into('=Bffffffff', plantDataTuple)
    except struct.error:
        return -1
