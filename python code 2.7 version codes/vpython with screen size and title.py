import serial #Import Serial Library
from visual import * #Import all the vPython library
myscreen= display(title='virtual world')
myscreen.width=1600
myscreen.height=1000
measuringRod = cylinder( title="My Meter", radius= 0.2, length=6, color=color.yellow, pos=(-3,0,0))
