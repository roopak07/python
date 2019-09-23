import serial #import Serial Library
from visual import *
screen=display(title='pot cylinder')
screen.width=1600
screen.height=1000
screen.range=(25,25,25)
arduinoSerialData = serial.Serial('com3', 9600)
cylinder=cylinder(color=color.blue,radius=1,length=10)
while(1==1):
    rate(20)
    if(arduinoSerialData.inWaiting()>0):
       myData = arduinoSerialData.readline()
       print myData
       data=float(myData)#if we dont convert it in to float value then it will through an error
       cylinder.length=data
       
       
