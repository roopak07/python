from visual import *
myscreen=display(title='box virtual')
myscreen.width=1600
myscreen.height=1000
myscreen.range=(12,12,12)
frontbox=box(length=0.1,width=10,height=5,color=color.green,pos=(6,0,0))
#if we make pos=(0,0,0) we cant see 3d box we can see only a straight line
backbox=box(length=0.1,width=10,height=5,color=color.green,pos=(-8.5,0,0))
downcylinder=cylinder(color=color.blue,pos=(-8.5,0,2.5),radius=1.5,length=2.5)
backcylinder=cylinder(color=color.blue,pos=(-8.5,0,-2.5),radius=1.5,length=2.5)
ball=sphere(color=color.red,radius=0.3)
