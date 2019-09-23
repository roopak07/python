import numpy as np
import matplotlib.pyplot as mp
x=np.linspace(-3,3,12) # linspace(start,stop,number points)
y=x**2
mp.plot(x,y,'bo-',label='y=x*2') #'bo' only dots ,'bo-' dots and lines
mp.legend()
mp.title('plot')
mp.xlabel('x axis')
mp.ylabel('y axis')
mp.show()
