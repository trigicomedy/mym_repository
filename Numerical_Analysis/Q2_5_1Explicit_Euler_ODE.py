import math
import numpy as np

def func(t,y):
    return y-2*t/y

def Euler_ODE(xspan,y0,h):
    y=y0
    n=int((xspan[1]-xspan[0])/h)
    for i in range(n):
        y+=h*func(xspan[0]+i*h,y)
        y=np.around(y,4)
        print(y)
    return y
if __name__=='__main__':
    h=0.2
    y1=Euler_ODE([0,1.0],1.0,h)
