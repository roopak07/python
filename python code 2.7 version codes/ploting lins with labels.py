import numpy as np
import matplotlib.pyplot as pt
x=[2,4,6,8]
y=[4,8,12,16] #this is in the form of y=2*x
z=[6,12,18,24] #this is in the form of z=3*x
pt.plot(x,'bo') #plots with respect to 0,1,2,3 i.e 0-2,1-4,2-6,3-8
pt.plot(x) #plots with respect to 0,1,2,3 i.e 0-2,1-4,2-6,3-8
pt.plot(y,'ro') #plots with respect to 0,1,2,3 i.e 0-4,1-8,2-12,3-16
pt.plot(y) #plots with respect to 0,1,2,3 i.e 0-4,1-8,2-12,3-16
pt.plot(z,'go') #plots with respect to 0,1,2,3 i.e 0-6,1-12,2-18,3-24
pt.plot(z) #plots with respect to 0,1,2,3 i.e 0-6,1-12,2-18,3-24
pt.plot(x,y,label='y=2*x') #plots with respect to x i.e 2-4,4-8,6-12,8-16
pt.plot(x,y,'o',label='y=2*x') #plots with respect to x i.e 2-4,4-8,6-12,8-16
pt.plot(x,z,label='z=3*x') #plots with respect to x i.e 2-6,4-12,6-18,8-24
pt.plot(x,z,'o',label='z=3*x') #plots with respect to x i.e 2-6,4-12,6-18,8-24
pt.title('diffrent lines plot')
pt.xlabel('x axis')
pt.ylabel('y axis')
pt.legend() #this fuction is for labeling label='y=2*x' , label='z=3*x'
pt.show()
