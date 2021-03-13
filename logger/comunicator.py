import serial
from time import sleep


class ProtoException(Exception):
    def __init__(self, raw, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rawline = raw


class Sensors:
    HUM = 'hum'
    SOIL = 'soil'
    TEMP = 'temp'
    ALL = [HUM, SOIL, TEMP]


def connect() -> serial.Serial:
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
    ser.flush()
    return ser


def get_data(cmd, ser) -> str:
    ser.write((cmd + '\n').encode('utf-8'))
    sleep(1)
    line = ser.readline().decode('utf-8').rstrip()
    return line


def read(sensor):
    ser = connect()
    to_check = None

    if isinstance(sensor, str):
        to_check = [sensor]
    elif isinstance(sensor, list):
        to_check = sensor
    else:
        raise ValueError

    to_return = ()
    for s in to_check:
        if s not in Sensors.ALL:
            raise ValueError
        line = get_data(s, ser)
        if s not in line:
            to_return += ProtoException(line)
        else:
            value = line.split(':')[1]
            value = float(value)
            to_return += (value,)

    ser.close()
    return dict(zip(to_check, to_return))
