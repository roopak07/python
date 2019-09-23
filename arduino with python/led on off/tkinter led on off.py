import serial
arduinoData = serial.Serial('com7',9600)
from Tkinter import *

def callback1():
    arduinoData.write('1')
    
def callback2():
   arduinoData.write('0')
   
led_control_window= Tk()   
btn=Button(led_control_window,text="led on",command=callback1)
btn2=Button(led_control_window,text="led off",command=callback2)
btn.pack()
btn2.pack()
mainloop()
