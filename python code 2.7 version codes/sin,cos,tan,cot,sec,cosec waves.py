import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,25)
y=np.sin(x)
z=np.cos(x)
t=np.tan(x)
u=np.arctan(x) #arc means inverse (cot=1/tan)
#s=np.arccos(x) # sec=1/cos 
#c=np.arcsin(x) #cosec=1/sin
plt.axis([0,2*np.pi,-1.5,1.5])
plt.title('wave forms')
plt.xlabel('pi values')
plt.ylabel('waves')
plt.plot(x,y,'o-',label='y=sin(x)')
plt.plot(x,z,'o-',label='z=cos(x)')
plt.plot(x,t,'o-',label='t=tan(x)')
plt.plot(x,u,'o-',label='u=cot(x)')
#plt.plot(x,s,'o-',label='s=sec(x)')
#plt.plot(x,c,'o-',label='c=cosec(x)')
plt.grid(True)
plt.legend()
plt.show()
