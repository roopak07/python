from Tkinter import *
led_control_window= Tk()
def callback1():
    print "led on"
def callback2():
    print "led off"
btn=Button(led_control_window,text="led on",command=callback1)
btn2=Button(led_control_window,text="led off",command=callback2)
btn.pack()
btn2.pack()
mainloop()
