import numpy as np
import matplotlib.pyplot as pt
x=np.arange(-3,3,0.5)
y=x**2
pt.plot(x,y,'o',label='y=2x')
pt.title('plot')
pt.xlabel('x axis')
pt.ylabel('y axis')
pt.legend()
pt.show()
