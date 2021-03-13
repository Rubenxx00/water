import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600
)

ser.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

inputstr=1
while 1 :
    # get keyboard input
    inputstr = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if inputstr == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write((inputstr + '\n').encode('utf-8'))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode('utf-8')

        if out != '':
            print (">>" + out)