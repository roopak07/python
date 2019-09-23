import serial #import Serial Library
arduinoSerialData = serial.Serial('com5', 9600) #arduinoSerialData is a variable
while(1==1):
       myData = arduinoSerialData.readline() #read data from arduino
       print myData #print on screen
input()
