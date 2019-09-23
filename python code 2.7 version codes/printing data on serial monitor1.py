import serial #import Serial Library
arduinoSerialData = serial.Serial('com7', 9600)
while(1==1):
    if(arduinoSerialData.inWaiting()>0):
       myData = arduinoSerialData.readline()
       print myData # one data print is enough for any number of serial prints in arduino code ,no need to mention delay in this code ,if we mention in arduino code then its enough 
