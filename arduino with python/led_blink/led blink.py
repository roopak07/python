import serial #Serail imported for Serial communication
import time #for time.sleep function

ArduinoSerial = serial.Serial('com5',9600) #starting serial communication at port 5 ,with baudrate 9600
time.sleep(2) # wait for 2 seconds 

print ArduinoSerial.readline() #read serial data from arduino and print on screen 
print ("Enter 1 to  turn ON LED and 0 turn OFF LED") # no connection with arduino ,we printing with python 

while 1: 
    var = raw_input() #get input from user
    print "You entered",var #print the input for confirmation

    if(var == '1'): # if the value is 1
        ArduinoSerial.write('1') # send 1 to Arduino 
        print ("LED turned ON") #print with python 
        time.sleep(1) # delay for 1 second 

    if(var == '0'): # if the value is 0
        ArduinoSerial.write('0') # send 0 to arduino
        print("LED turned OFF") # print with pyhton
