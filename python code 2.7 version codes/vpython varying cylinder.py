import serial #import Serial Library
from visual import *
screen=display(title='pot cylinder')
screen.width=1600
screen.height=1000
screen.range=(12,12,12)
arduinoSerialData = serial.Serial('com6', 9600)
cylinder=cylinder(title='cylinder',color=color.blue,radius=1,length=10)
while(1==1):
    rate(20) #we we wont us rate it will through an error, rate means "Tell vpython to run this loop 20 times a second"
    if(arduinoSerialData.inWaiting()>0):
       myData = arduinoSerialData.readline()
       print myData
       data=float(myData)#if we dont convert it in to float value then it will through an error
       cylinder.length=data #we can change any variable by using .pos or .length or .heigth or .radius etc
       
       
