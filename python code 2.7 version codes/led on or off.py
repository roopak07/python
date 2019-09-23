import serial

arduinoData = serial.Serial('com5',9600)
print arduinoData.readline()

while 1:
     arduinoData.write('1') #if we want to off then replace 1 with 0



