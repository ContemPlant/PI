import serial
import struct
serialPort = '/dev/tty.usbserial-DN02MLF3'


def serial_data(port, baudrate):
    ser = serial.Serial(port, baudrate)

    while True:
        yield ser.readline()[:-1]

    ser.close()


def parseBytes(bytes):
    try:
        return struct.unpack_from('=BBLBBfff', bytes)
    except struct.error:
        return -1


def sensorDates():
    for line in serial_data(serialPort, 9600):
        yield parseBytes(line)
