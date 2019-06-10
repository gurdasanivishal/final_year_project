import serial
ser = serial.Serial('COM4', 9600, timeout=0)
while 1:
    var = raw_input("Enter 0 or 1 to control led: ")
    ser.write(var)
