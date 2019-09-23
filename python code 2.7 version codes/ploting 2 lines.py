import numpy as np
import matplotlib.pyplot as pt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
pt.plot(x) #plots x with respect to 0,1,2
pt.plot(y,'r^')#r=red line ,^ = triangle ,#plots y with respect to 0,1,2
pt.plot(x,y,'g--')#plots x with respect to y,o- =orange line,g=green line, -- = doted lines
pt.plot(x,y,'bo') #plots x with respect to y,b=blue color,o=display's dots 
pt.title('basic plot')
pt.xlabel('x axis')
pt.ylabel('y axis')
#pt.axis([0,10, 0,10]) # x axis will be 0 to 10 and y axis will be 0 to 10
pt.grid(True)#disply's grid lines
pt.show() #display's all plots,any plots,titles,labels etc below pt.show wont be displayed

