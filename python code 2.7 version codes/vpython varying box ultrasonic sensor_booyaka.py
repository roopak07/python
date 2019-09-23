from visual import *
import serial
screen=display(title='virtual')
screen.width=1600
screen.height=1000
screen.range=(20,20,20)
fbox=box(length=2,height=4,width=10,color=color.white,pos=(-15,0,0))
dcylinder=cylinder(radius=1.5,length=0.1,pos=(-14.01,0,-2.5),color=color.black)
fcylinder=cylinder(radius=1.5,length=0.1,pos=(-14.01,0,2.5),color=color.black)
vbox=box(length=0.1,height=6,width=9,pos=(-14,0,0),color=color.red)
ball=sphere(color=color.red,radius=0.5)
distancelabel=label(pos=(0,8,0),text='virtual object distance is:',height=30,color=color.blue)
light=cylinder(color=color.red,radius=0.3,length=0.01,pos=(-14.0,1,0))
arduino_data=serial.Serial('com21',9600)
while(1):
    rate(20)
    if(arduino_data.inWaiting()>0):
        sensor_data=arduino_data.readline() #data is recived in String formate
        print sensor_data
        data=float(sensor_data) #converting string to float value
        vbox.pos=vector(-14+data,0,0)
        mylabel='virtual distance between objects is:'+sensor_data +'cm'
        distancelabel.text=mylabel
