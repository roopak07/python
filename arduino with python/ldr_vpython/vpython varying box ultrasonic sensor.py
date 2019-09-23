from visual import *
import serial #import Serial Library
myscreen=display(title='box virtual')
myscreen.width=1600
myscreen.height=1000
myscreen.range=(20,20,20)
arduinoSerialData = serial.Serial('com3', 9600)
frontbox=box(length=0.1,width=10,height=5,color=color.green,pos=(-6,0,0))
#if we make pos=(0,0,0) we cant see 3d box we can see only a straight line
backbox=box(length=0.1,width=10,height=5,color=color.green,pos=(-8.5,0,0))
downcylinder=cylinder(color=color.blue,pos=(-8.5,0,2.5),radius=1.5,length=2.5)
backcylinder=cylinder(color=color.blue,pos=(-8.5,0,-2.5),radius=1.5,length=2.5)
ball=sphere(color=color.red,radius=0.3)
while(1==1):
    rate(20)
    if(arduinoSerialData.inWaiting()>0):
       myData = arduinoSerialData.readline()
       print myData
       data=float(myData)#if we dont convert it in to float value then it will through an error
       frontbox.pos=vector(-6 + data,0,0) #varry x position 
