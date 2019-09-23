import serial #import Serial Library
from visual import *
screen=display(title='pot cylinder')
screen.width=1600
screen.height=1000
screen.range=(12,12,12)
arduinoSerialData = serial.Serial('com6', 9600)
box=box(color=color.blue,width=8,height=5,length=0.1,pos=(-10,0,0))
while(1==1):
    rate(20)
    if(arduinoSerialData.inWaiting()>0):
       myData = arduinoSerialData.readline()
       print myData
       data=float(myData)#if we dont convert it in to float value then it will through an error
       box.pos=vector(-6 + data,0,0) #varry x position 
       
       
