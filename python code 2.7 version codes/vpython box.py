from visual import *
myscreen=display(title='box virtual')
myscreen.width=1600
myscreen.height=1000
myscreen.range=(10,10,10)
box=box(length=0.1,width=10,height=5,color=color.green,pos=(-5,0,0))
#if we make pos=(0,0,0) we cant see 3d box we can see only a straight line
