import numpy as np
import matplotlib.pyplot as mp
x=np.linspace(0,2*np.pi,25)
print x
y=np.sin(x)
print y
mp.xlabel('pi values')
mp.ylabel('sin valies')
mp.title('sine wave')
mp.grid(True)
mp.axis([0,2*np.pi,-1.5,1.5])
mp.plot(x,y,'bo-',label='y=sin(x)')
mp.legend()
mp.show()
