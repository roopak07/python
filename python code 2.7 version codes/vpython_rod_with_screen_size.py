import serial #Import Serial Library
from visual import * #Import all the vPython library
myscreen=display(title='my virtual world')
myscreen.width=800
myscreen.height=800
myscreen.range=(12,12,12)
measuringRod = cylinder( title="My Meter", radius= 0.2, length=6, color=color.yellow, pos=(-3,0,0))

